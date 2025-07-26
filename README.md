# 🎬 YouTube LLM Summarizer

This project extracts transcripts from YouTube videos, restores punctuation, cleans the text, and summarizes the content using a lightweight LLM via the OpenRouter API.

---

## 🚀 Features

- Extracts raw transcripts from YouTube videos (using `youtube-transcript-api`)
- Restores punctuation using `DeepMultilingualPunctuation`
- Cleans and preprocesses transcript text
- Generates high-quality summaries using OpenRouter's LLMs (e.g., Mistral, Claude)
- Runs efficiently even on low-end devices (like MacBook Air M2 with 8GB RAM)

---

## 📌 Why is this useful?

- Saves time by summarizing long video content
- Useful for students, researchers, and content creators
- Can handle multi-lingual content
- Lightweight design avoids heavy local models — perfect for laptops

---

## 🛠️ Tech Stack

- Python 3.12+
- `youtube-transcript-api`
- `deepmultilingualpunctuation`
- OpenRouter API for LLM summarization
- `transformers`, `torch`, `dotenv`

---

## 🧪 How to Use

1. Clone the repo:
   ```bash
   git clone https://github.com/yourusername/youtube-llm-summarizer.git
   cd youtube-llm-summarizer
