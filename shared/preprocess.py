import re
import emoji

def clean_text(text):
    """Basic cross-lingual social media text cleaning."""
    if not isinstance(text, str):
        return ""
    text = text.lower()
    text = re.sub(r"http\S+", "", text)    # remove URLs
    text = emoji.replace_emoji(text, replace='')  # remove emojis
    text = re.sub(r"#(\w+)", r"\1", text)  # split hashtags
    text = re.sub(r"\s+", " ", text)
    return text.strip()

