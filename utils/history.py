# utils/history.py

def save_user_message(redis_client, user_id: str, role: str, message: str):
    MAX_HISTORY = 10
    key = f"chat_history:{user_id}"
    redis_client.rpush(key, f"{role}: {message}")
    redis_client.ltrim(key, -MAX_HISTORY, -1)

def get_user_history(redis_client, user_id: str):
    key = f"chat_history:{user_id}"
    return redis_client.lrange(key, 0, -1)
