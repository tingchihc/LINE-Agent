import os
from redis import Redis
from dotenv import load_dotenv

env_path = os.path.join(os.path.dirname(__file__), '..', '.env')
load_dotenv(dotenv_path=env_path)

REDIS_HOST = os.getenv("REDIS_HOST")
REDIS_PORT = int(os.getenv("REDIS_PORT"))
DB = int(os.getenv("db"))

try:
    print(f"[DEBUG] host={REDIS_HOST}, port={REDIS_PORT}, db={DB}")

    redis_client = Redis(host=REDIS_HOST, port=REDIS_PORT, db=DB)
    redis_client.ping()

except Exception as e:
    print("[Redis 連線失敗]", e)
    raise