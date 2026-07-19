import re


def clean_text(text: str) -> str:
    """
    Clean extracted resume text.
    """

    # Replace multiple newlines with a single newline
    text = re.sub(r"\n+", "\n", text)

    # Replace multiple spaces with one space
    text = re.sub(r"[ \t]+", " ", text)

    # Remove leading/trailing whitespace
    text = text.strip()

    return text