from openai import OpenAI
import numpy as np
from pymongo import MongoClient
from dotenv import load_dotenv
import os
import json

env_path = os.path.join(os.path.dirname(__file__), '..', '.env')
load_dotenv(dotenv_path=env_path)

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
DEPLOYMENT_NAME = os.getenv("deployment_name")

MONGODB = os.getenv("MONGODB")

def get_embedding(text):
    response = clinent.embeddings.create(
        input=[text],
        model="text-embedding-3-small"
    )
    
    return np.array(response.data[0].embedding)

def connect_pymongo(database='dotdot'):
    myclient = MongoClient(MONGODB)
    mydb = myclient[database]

    return myclient, mydb

clinent = OpenAI()

"""
qa_upload = []
with open("/home/user/TC/workstation/multi_agents_system/docs/qa.json", "r") as f:
    qa = json.load(f)
for id_, info in qa.items():
    q, a = info[0], info[-1]
    q_emb = get_embedding(q)
    qa_upload.append({"question": q, "q_emb": q_emb.tolist(), "answer": a})
"""

client, db = connect_pymongo()

#db["qa_set"].insert_many(qa_upload)

"""
new_upload = []
with open("/home/user/TC/workstation/multi_agents_system/docs/news_info.json", "r") as f:
    news = json.load(f)
for id_, info in news.items():
    topic_emb = get_embedding(info["topic"])
    new_upload.append({"topic": info["topic"],
                       "time": info["time"],
                       "content": info["content"],
                       "topic_emb": topic_emb.tolist()})

db["news"].insert_many(new_upload)
"""