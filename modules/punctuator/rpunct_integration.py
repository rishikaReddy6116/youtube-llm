# modules/punctuator/rpunct_integration.py

from deepmultilingualpunctuation import PunctuationModel

# Load the lightweight punctuation model
model = PunctuationModel()

def restore_punctuation(text: str) -> str:
    """
    Restore punctuation in a given unpunctuated text using the DeepMultilingualPunctuation model.

    Args:
        text (str): Raw transcript text without punctuation.

    Returns:
        str: Punctuated text.
    """
    return model.restore_punctuation(text)
