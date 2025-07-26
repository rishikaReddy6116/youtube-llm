def clean_transcript(text):
    """
    Cleans the raw transcript text by removing unwanted characters or repeated spaces.
    You can expand this function as needed.
    """
    import re
    cleaned = re.sub(r'\s+', ' ', text)  # remove extra whitespace
    return cleaned.strip()
