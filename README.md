# 🎬 YouTube LLM Summarizer

This project extracts transcripts from YouTube videos, restores punctuation, cleans the text, and generates a clear, concise summary using lightweight LLMs via the OpenRouter API.

---

## ✅ Why This Project?

- 🔍 **Problem**: YouTube videos can be long and time-consuming to watch, especially when you're just looking for the key points.
- 💡 **Solution**: This tool automates transcript extraction and summarization — giving you a quick understanding of video content without watching it.
- ⚡ **Efficiency**: Designed to run even on low-resource machines (e.g., MacBook Air M2 with 8GB RAM), by using lightweight tools and external APIs instead of heavy local models.

---

## 🛠️ How to Run

1. **Clone the repository:**
   ```bash
   https://github.com/rishikaReddy6116/youtube-llm-summarizer

2. Install dependencies:   
   bash
   Copy
   Edit
   pip install -r requirements.txt
   
4. Add your OpenRouter API key:
   Create a .env file in the root directory and add:
   ini
   Copy
   Edit
   OPENROUTER_API_KEY=your_api_key_here
   
6. Run the summarizer:
   bash
   Copy
   Edit
   python main.py

7. Enter any YouTube video link or ID when prompted.
