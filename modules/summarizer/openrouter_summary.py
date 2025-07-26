import os
import requests

def get_openrouter_summary(prompt: str) -> str:
    api_key = os.getenv("OPENROUTER_API_KEY")
    if not api_key:
        raise Exception("Missing OPENROUTER_API_KEY in environment.")

    headers = {
        "Authorization": f"Bearer {api_key}",
        "HTTP-Referer": "youtube-llm",  # optional
        "Content-Type": "application/json",
    }

    payload = {
        "model": "gpt-3.5-turbo",  # ✅ CORRECTED model ID
        "messages": [
            {"role": "system", "content": "Summarize the following transcript."},
            {"role": "user", "content": prompt},
        ],
    }

    response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=payload)

    if response.ok:
        return response.json()["choices"][0]["message"]["content"]
    else:
        raise Exception(f"OpenRouter API Error: {response.text}")
