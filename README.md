
# Document QA Chatbot with Pinecone and Hugging Face

This project is a document-based Question Answering (QA) chatbot that allows users to upload PDF documents and ask questions. The chatbot retrieves relevant document segments from Pinecone and generates answers using Hugging Face's question-answering model.

## Features:
- Upload PDF files
- Extract text from uploaded PDFs
- Store document embeddings in Pinecone vector database
- Ask questions and get answers using context from the document
- Real-time document retrieval and QA using Hugging Face models
- Supports multiple queries after uploading a PDF
- Built with Streamlit for a simple user interface

## Technologies Used:
- **Python**: Backend logic and integration
- **Streamlit**: Frontend for user interaction
- **Pinecone**: Vector database for storing and retrieving document embeddings
- **Hugging Face Transformers**: Pre-trained models for generating QA answers
- **SentenceTransformers**: For embedding the PDF text and user queries
- **PyMuPDF**: For extracting text from PDF files

---

## Requirements

- Python 3.9+
- Pinecone API Key
- OpenAI API Key or any relevant embedding model

---

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/document-qa-chatbot.git
cd document-qa-chatbot
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Pinecone API Setup

To integrate with Pinecone, you'll need to:
1. Sign up at [Pinecone.io](https://www.pinecone.io) and retrieve your **Pinecone API key**.
2. Add the following code in `streamlit_app.py`:
```python
pinecone.init(api_key="YOUR_PINECONE_API_KEY", environment="us-west1-gcp")
```

### 4. Hugging Face Model

The project uses a Hugging Face model (`deepset/roberta-base-squad2`) for the QA task. You can replace this model with any other Hugging Face question-answering model if desired.

```python
qa_pipeline = pipeline("question-answering", model="deepset/roberta-base-squad2")
```

### 5. Run the Application

To start the Streamlit app:

```bash
streamlit run streamlit_app.py
```

Open your browser and navigate to `http://localhost:8501`. You will see the interface where you can upload PDFs and ask questions.

### 6. Dockerize (Optional)

If you want to containerize the application using Docker:

1. Build the Docker image:
   ```bash
   docker build -t pdf-qa-chatbot .
   ```

2. Run the Docker container:
   ```bash
   docker run -p 8501:8501 pdf-qa-chatbot
   ```

---

## How to Use the Application

1. **Upload PDF**: Drag and drop or upload a PDF document.
2. **Processing PDF**: The application will extract the text and generate embeddings for the document.
3. **Ask Questions**: Type your question in the input box.
4. **View Answer**: The chatbot will display the generated answer along with the retrieved document context.

---

## Project Structure

```
├── app
│   ├── __init__.py
│   ├── document_retrieval.py  # Contains functions for text extraction, embedding, and querying Pinecone
├── streamlit_app.py  # Main Streamlit app
├── requirements.txt  # Project dependencies
├── Dockerfile  # Docker configuration for containerizing the application
└── README.md  # Project documentation
```

### `document_retrieval.py`

This file contains utility functions for:
- **`extract_text_from_uploaded_pdf()`**: Extracts text from a PDF using `PyMuPDF`.
- **`generate_embeddings()`**: Uses SentenceTransformers to generate document embeddings.
- **`store_embeddings_in_pinecone()`**: Stores document embeddings in Pinecone for later retrieval.
- **`query_pinecone()`**: Queries Pinecone to retrieve relevant document segments based on user questions.
- **`generate_answer()`**: Uses Hugging Face models to generate answers from the retrieved context.

---

## Deployment Instructions

### Docker Deployment:

To make deployment easier, the app is containerized using Docker.

1. **Build Docker Image:**
   ```bash
   docker build -t pdf-qa-chatbot .
   ```

2. **Run Docker Container:**
   ```bash
   docker run -p 8501:8501 pdf-qa-chatbot
   ```

3. Visit `http://localhost:8501` in your browser to access the chatbot.

### API Keys:

Ensure you have set up the following environment variables for your deployment:
- `PINECONE_API_KEY`
- `OPENAI_API_KEY` (if you use OpenAI's embedding models)
  
Alternatively, you can replace the OpenAI key with a Hugging Face-compatible sentence transformer for embedding generation.

---

## Example Interaction

1. **Upload PDF**: Upload a sample offer letter PDF.
2. **Ask Question**: "What is the offered salary?"
3. **View Answer**: "The offered salary is $60,000 per annum."
4. **Retrieved Document Segment**: "We are pleased to offer you a salary of $60,000 annually..."

---

## Future Improvements

- Implement handling for large documents by splitting text into smaller chunks and storing them as separate embeddings.
- Allow for multi-file uploads and querying across multiple documents.
- Optimize embedding and retrieval for improved performance on large-scale documents.

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Contributions

Contributions are welcome! Please create a pull request or open an issue for any improvements or suggestions.

---

## Author
Vinay Sharma 