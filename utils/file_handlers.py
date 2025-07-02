import PyPDF2
from docx import Document

def extract_text(uploaded_file):
    if uploaded_file.type == "text/plain":
        return uploaded_file.getvalue().decode("utf-8")
    elif uploaded_file.type == "application/pdf":
        pdf_reader = PyPDF2.PdfReader(uploaded_file)
        return " ".join([page.extract_text() for page in pdf_reader.pages])
    elif "wordprocessingml" in uploaded_file.type:  # DOCX
        doc = Document(uploaded_file)
        return "\n".join([para.text for para in doc.paragraphs])
    return "Unsupported file type"

