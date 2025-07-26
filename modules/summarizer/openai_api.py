import os
import requests
from dotenv import load_dotenv

# Load .env variables
load_dotenv()

def generate_summary(text: str) -> str:
    if not text.strip():
        return "Transcript is empty or invalid."

    # DEBUG: Print API key (you can remove this after testing)
    print("API KEY:", os.getenv("OPENROUTER_API_KEY"))

    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {os.getenv('OPENROUTER_API_KEY')}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "mistralai/mistral-7b-instruct",
        "messages": [{"role": "user", "content": f"Summarize this YouTube transcript:\n\n{text}"}],
        "temperature": 0.5
    }

    response = requests.post(url, headers=headers, json=data)
    response.raise_for_status()
    return response.json()["choices"][0]["message"]["content"].strip()
