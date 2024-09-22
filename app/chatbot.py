# app/chatbot.py
from app.document_retrival import extract_text_from_uploaded_pdf
from app.answer_generation import generate_answer

def ask_question_from_pdf(uploaded_pdf, question):
    """Ask question based on the content of the uploaded PDF."""
    context = extract_text_from_uploaded_pdf(uploaded_pdf)
    answer = generate_answer(context, question)
    return answer
