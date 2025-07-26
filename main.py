import os
from dotenv import load_dotenv

from modules.transcript.transcript_extractor import get_youtube_transcript
from modules.punctuator.restoration import restore
from modules.punctuator.postprocessing import clean_text
from modules.summarizer.openrouter_summary import get_openrouter_summary
from textwrap import fill

def run_pipeline(video_input: str):
    print("🔹 Extracting transcript...")
    raw_text = get_youtube_transcript(video_input)

    print("🔹 Restoring punctuation...")
    punctuated_text = restore(raw_text)

    print("🔹 Cleaning text...")
    cleaned_text = clean_text(punctuated_text)

    print("🔹 Summarising with OpenRouter...")
    summary = get_openrouter_summary(cleaned_text)

# Clean and format the summary into a readable paragraph
    formatted_summary = fill(summary.strip(), width=100)
    print("\n✅ Final Summary:\n")
    print(formatted_summary)


if __name__ == "__main__":
    load_dotenv()
    test_video_input = input("🔗 Enter YouTube video URL or ID: ").strip()
    run_pipeline(test_video_input)
