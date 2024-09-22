# app/answer_generation.py
import cohere
from config.config import COHERE_API_KEY

def generate_answer(context, question):
    """Generate an answer using the Cohere API."""
    cohere_client = cohere.Client(COHERE_API_KEY)
    
    prompt = f"Based on the following context:\n{context}\n\nAnswer this question: {question}"
    
    response = cohere_client.generate(
        model='command',  # Or any model you are using
        prompt=prompt,
        max_tokens=200  # Limit the response length
    )
    
    return response.generations[0].text.strip()
