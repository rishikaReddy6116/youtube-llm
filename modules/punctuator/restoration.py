# modules/punctuator/restoration.py

from .rpunct_integration import restore_punctuation

def restore(text: str) -> str:
    """
    Wrapper function to restore punctuation in raw text.

    Args:
        text (str): Transcript without punctuation.

    Returns:
        str: Punctuated transcript.
    """
    return restore_punctuation(text)
