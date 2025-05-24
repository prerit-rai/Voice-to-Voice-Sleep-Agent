import openai
from config import OPENAI_API_KEY
openai.api_key = OPENAI_API_KEY


def embed_and_store_faqs():
    sleep_questions = [
        "What is deep sleep?",
        "How can I improve REM sleep?",
        "Why do I wake up at night?"
    ]
    vectors = [
        openai.Embedding.create(input=q, model="text-embedding-ada-002") for q in sleep_questions
    ]
    return vectors

# Optional call
if __name__ == '__main__':
    embed_and_store_faqs()
