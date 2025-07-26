# modules/punctuator/postprocessing.py

import re

def clean_text(text: str) -> str:
    """
    Basic postprocessing: removes extra spaces, repeated punctuation, and normalizes text.

    Args:
        text (str): Input text.

    Returns:
        str: Cleaned text.
    """
    # Replace multiple spaces with one
    text = re.sub(r'\s+', ' ', text)

    # Remove repeated punctuation (e.g., "!!", "..", "??")
    text = re.sub(r'([?.!,]){2,}', r'\1', text)

    # Fix spacing before punctuation
    text = re.sub(r'\s+([?.!,])', r'\1', text)

    return text.strip()
