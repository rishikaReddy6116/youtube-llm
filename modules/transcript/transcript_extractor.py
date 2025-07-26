from youtube_transcript_api import YouTubeTranscriptApi
import re

def extract_video_id(url: str) -> str:
    """
    Extract the video ID from a full YouTube URL or return the input if it's already an ID.
    """
    if re.match(r"^[a-zA-Z0-9_-]{11}$", url):
        return url  # already an ID
    match = re.search(r"(?:v=|youtu\.be/)([a-zA-Z0-9_-]{11})", url)
    if match:
        return match.group(1)
    raise ValueError("Invalid YouTube URL or ID")

def get_youtube_transcript(video_input: str) -> str:
    video_id = extract_video_id(video_input)
    transcript = YouTubeTranscriptApi.get_transcript(video_id)
    return " ".join([entry['text'] for entry in transcript])
