import os
from redis import Redis
import asyncio
from dotenv import load_dotenv

from fastapi import FastAPI, Request, Header, HTTPException
from fastapi.concurrency import run_in_threadpool

from utils.agents import triage_agent
from utils.search_topics import search_related
from utils.history import save_user_message, get_user_history

from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

app = FastAPI()

load_dotenv()

LINE_CHANNEL_ACCESS_TOKEN = os.getenv("LINE_CHANNEL_ACCESS_TOKEN")
LINE_CHANNEL_SECRET = os.getenv("LINE_CHANNEL_SECRET")

REDIS_HOST = os.getenv("REDIS_HOST")
REDIS_PORT = int(os.getenv("REDIS_PORT"))
DB = int(os.getenv("db"))

line_bot_api = LineBotApi(LINE_CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(LINE_CHANNEL_SECRET)

redis_client = Redis(host=REDIS_HOST, port=REDIS_PORT, db=DB, decode_responses=True)

@app.get("/health_check")
async def health_check():
    """
    make sure API is working
    """
    response={
                "Method": "GET",
                "State": "Success",
                "Data": "healthy",
                "message": "GET Success"
            }
    return response

@app.post("/webhook")
async def webhook(request: Request, x_line_signature: str = Header(None)):
    body = await request.body()
    try:
        handler.handle(body.decode("utf-8"), x_line_signature)
    except InvalidSignatureError:
        raise HTTPException(status_code=400, detail="Invalid signature")
    return "OK"

async def process_message(event):
    user_id = event.source.user_id
    user_message = event.message.text

    save_user_message(redis_client, user_id, "User", user_message)

    history = get_user_history(redis_client, user_id)
    history_text = "\n".join(history)

    related_info = search_related(user_message)

    messages = f"{related_info}\n{history_text}\nUser: {user_message}\nAI:"

    response = await triage_agent.get_response(messages=messages, thread=None)
    ai_reply = response.items[0].text if response.items else "Sorry, I cannot understand your question."

    save_user_message(redis_client, user_id, "AI", ai_reply)

    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=ai_reply)
    )

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    asyncio.create_task(process_message(event))

@app.get("/chatbot_response")
async def chatbot_response(question: str):
    
    messages = search_related(question)        
    messages += f"\n\User: {question}"
    response = await triage_agent.get_response(
        messages=messages,
        thread=None,
    )

    text = response.items[0].text if response.items else ""

    return {"answer": text}
