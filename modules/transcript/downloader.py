from youtube_transcript_api import YouTubeTranscriptApi

def extract_transcript(video_url):
    try:
        video_id = video_url.split("watch?v=")[-1]
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        return " ".join([line["text"] for line in transcript])
    except Exception as e:
        raise RuntimeError(f"Transcript Error: {e}")
