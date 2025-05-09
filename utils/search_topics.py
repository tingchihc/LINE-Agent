from openai import OpenAI
import numpy as np
import os
from dotenv import load_dotenv
from .get_DB import get_info


env_path = os.path.join(os.path.dirname(__file__), '..', '.env')
load_dotenv(dotenv_path=env_path)
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
DEPLOYMENT_NAME = os.getenv("deployment_name")
clinent = OpenAI()

def get_embedding(text):
    response = clinent.embeddings.create(
        input=[text],
        model="text-embedding-3-small"
    )
    
    return np.array(response.data[0].embedding)

def cosine_similarity(vec1, vec2):
    return np.dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2))

def search_related(user_input):
    #web_stored_embeddings, web_content = [], []
    #website_data = get_info("website")
    #for w in website_data:
    #    web_stored_embeddings.append(w['embeddings'])
    #    web_content.append(w['content'])
    
    #news_stored_embeddings, news_content = [], []
    #news_data = get_info("news")
    #for n in news_data:
    #    news_stored_embeddings.append(n['topic_emb'])
    #    news_content.append(n['content'])
    
    qa_stored_embeddings, qa_content = [], []
    qa_data = get_info("qa_set")
    for q in qa_data:
        qa_stored_embeddings.append(q['q_emb'])
        qa_content.append(q['answer'])

    user_input_emb = get_embedding(user_input)
    similarities = [cosine_similarity(user_input_emb, emb) for emb in qa_stored_embeddings]
    top_indices = np.argsort(similarities)[::-1][:5]
    similarity_threshold = 0.7
    use_examples = similarities[top_indices[0]] >= similarity_threshold

    examples = "\n".join([
            f"內容：{qa_content[i]}"
            for i in top_indices if similarities[i] >= similarity_threshold
        ]) if use_examples else "（這次沒有相近的範例，請直接根據知識回答。）"

    return examples
