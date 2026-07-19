import re

# Start with a curated list. We'll expand this over time.
COMMON_SKILLS = [
    "python",
    "sql",
    "pandas",
    "numpy",
    "streamlit",
    "fastapi",
    "flask",
    "django",
    "docker",
    "kubernetes",
    "git",
    "github",
    "linux",
    "aws",
    "azure",
    "gcp",
    "power bi",
    "tableau",
    "excel",
    "openai",
    "langchain",
    "rag",
    "machine learning",
    "deep learning",
    "tensorflow",
    "pytorch",
]


def extract_skills(text: str):
    """
    Extract known skills from text.
    """
    text = text.lower()

    found = set()

    for skill in COMMON_SKILLS:
        pattern = r"\b" + re.escape(skill) + r"\b"

        if re.search(pattern, text):
            found.add(skill.title())

    return sorted(found)