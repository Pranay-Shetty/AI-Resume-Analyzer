from docx import Document


def extract_docx_text(uploaded_file):
    """Extract text from a DOCX file."""

    document = Document(uploaded_file)

    text = ""

    for paragraph in document.paragraphs:
        text += paragraph.text + "\n"

    return text