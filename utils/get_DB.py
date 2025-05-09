from pymongo import MongoClient
from dotenv import load_dotenv
import os

env_path = os.path.join(os.path.dirname(__file__), '..', '.env')
load_dotenv(dotenv_path=env_path)

MONGODB = os.getenv("MONGODB")

def connect_pymongo(database='dotdot'):
    myclient = MongoClient(MONGODB)
    mydb = myclient[database]

    return myclient, mydb

def get_info(collection_name):
    client, db = connect_pymongo()
    col = db[collection_name]
    
    return list(col.find())
