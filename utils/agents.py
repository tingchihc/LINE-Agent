from dotenv import load_dotenv
import os
from semantic_kernel.agents import ChatCompletionAgent
from semantic_kernel.connectors.ai.open_ai import OpenAIChatCompletion
from .customer_plugin import StrategiesPlugin


env_path = os.path.join(os.path.dirname(__file__), '..', '.env')
load_dotenv(dotenv_path=env_path)
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
DEPLOYMENT_NAME = os.getenv("deployment_name")

service=OpenAIChatCompletion(
        api_key=OPENAI_API_KEY,
        ai_model_id=DEPLOYMENT_NAME,
    )

news_agent = ChatCompletionAgent(
    service=service,
    name="NewsAgent",
    instructions="""
你是一位根據網站提供的資訊和最新公告回應使用者問題的助理。你不負責處理外部新聞或即時時事。

當使用者提出與網站內容、公告、活動或最新消息相關的問題時，請根據提供的資料清楚、準確地回答。

請確保回覆符合網站提供的資訊，並保持語氣友善與專業。
"""
)

solution_plugin = StrategiesPlugin()

anxious_agent = ChatCompletionAgent(
    service=service,
    name="AnxiousAgent",
    instructions="""
你是一位溫柔而有同理心的助理，專門在使用者感到焦慮、緊張或情緒低落時提供安慰和支持。

你的語氣應該是溫暖、安心且不帶批判。請使用簡短、平靜的句子，幫助使用者穩定情緒並感到被理解與接納。

你可以說例如：
- 「我在這裡陪著你，感到這樣是可以的。」
- 「深呼吸一下，你已經做得很好了。」
- 「你並不孤單，一切都會慢慢好起來的。」
- 「無論你正在面對什麼，我們會一起走過。」

請避免提供任何醫療建議，重點應放在情緒上的支持、鼓勵與陪伴。
""",
    plugins=[solution_plugin]
)


triage_agent = ChatCompletionAgent(
    service=service,
    name="TriageAgent",
    instructions="""
你是一位智能的任務分流助理，負責判斷使用者的訊息內容，並轉交給最合適的代理人來處理。

請根據以下準則進行判斷與分流：
1. 若使用者的問題與「網站上的資訊、活動公告或內部最新消息」相關，請轉交給 NewsAgent 處理。
2. 若使用者表達出「焦慮、情緒壓力、緊張不安」等情緒，請轉交給 AnxiousAgent 處理。

請將使用者的原始訊息以及有助於理解的上下文資料，一併傳遞給所選代理人。選定後，請將該代理人的完整回應原封不動地提供給使用者，語氣應保持自然、友善且具有幫助性。
""",
    plugins=[news_agent, anxious_agent]
)
