# streamlit_app.py
import streamlit as st
from app.chatbot import ask_question_from_pdf

# Streamlit app configuration
st.title("QA Chatbot for PDF Documents")
st.write("Upload a PDF file and ask any questions about its content!")

# PDF upload
uploaded_pdf = st.file_uploader("Upload a PDF", type=["pdf"])

if uploaded_pdf is not None:
    st.write("PDF Uploaded Successfully!")

    # Input question
    question = st.text_input("Enter your question about the document")

    if question:
        with st.spinner('Generating answer...'):
            # Ask question based on uploaded PDF
            answer = ask_question_from_pdf(uploaded_pdf, question)
            st.write(f"**Answer**: {answer}")
