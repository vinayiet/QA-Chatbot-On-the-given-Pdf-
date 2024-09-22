# app/document_retrieval.py
import PyPDF2
from io import BytesIO

def extract_text_from_uploaded_pdf(uploaded_file):
    """Extracts text from an uploaded PDF file."""
    text = ""
    reader = PyPDF2.PdfReader(uploaded_file)
    for page_num in range(len(reader.pages)):
        text += reader.pages[page_num].extract_text()
    return text