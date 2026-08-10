# 🎓 EduRAG – AI University Document Assistant

EduRAG is a Retrieval-Augmented Generation (RAG) application that allows users to upload university PDF documents and ask natural-language questions about their contents.

The system automatically extracts and chunks document text, generates embeddings, stores them in a vector database, retrieves relevant information, and uses a local Large Language Model to generate grounded answers with source citations.

## ✨ Features

- Upload university PDF documents through a React interface
- Automatic PDF text extraction and indexing
- Text chunking for semantic retrieval
- Sentence Transformer embeddings
- ChromaDB vector storage
- Semantic similarity search
- Retrieval-Augmented Generation (RAG)
- Local LLM inference using Ollama and Llama 3.2
- Multi-document retrieval
- Source document and page citations
- Grounded responses with fallback handling
- FastAPI REST backend
- React + Vite frontend

## 🏗️ Architecture

User
↓
React Frontend
↓
FastAPI Backend
↓
PDF Extraction
↓
Text Chunking
↓
Sentence Transformer Embeddings
↓
ChromaDB Vector Store
↓
Semantic Retrieval
↓
Llama 3.2 via Ollama
↓
Grounded Answer + Sources

## 🛠️ Technology Stack

### Backend
- Python
- FastAPI
- LangChain
- ChromaDB
- Sentence Transformers
- Ollama
- Llama 3.2

### Frontend
- React
- Vite
- Axios
- CSS

## 🔄 How EduRAG Works

1. The user uploads a PDF through the React frontend.
2. FastAPI validates and stores the uploaded document.
3. Text is automatically extracted from the PDF.
4. Extracted text is divided into smaller chunks.
5. Embeddings are generated for the document chunks.
6. Chunks and metadata are stored in ChromaDB.
7. The user asks a question.
8. The question is converted into an embedding and relevant chunks are retrieved using semantic similarity.
9. Retrieved context and the question are passed to Llama 3.2 through Ollama.
10. The generated answer is returned with the relevant document name and page number.

## 📁 Project Structure

```text
EduRAG/
├── backend/
│   ├── app/
│   │   ├── api/
│   │   ├── core/
│   │   ├── rag/
│   │   ├── schemas/
│   │   └── services/
│   └── requirements.txt
│
├── frontend/
│   ├── src/
│   │   ├── api/
│   │   ├── components/
│   │   ├── App.jsx
│   │   └── App.css
│   └── package.json
│
└── README.md
🚀 Running Locally
Backend

Create and activate a Python virtual environment, then install the dependencies:

cd backend
pip install -r requirements.txt

Start Ollama and make sure the required model is available:

ollama pull llama3.2:3b

Run the FastAPI application:

python -m uvicorn app.main:app --reload

The API will run locally on port 8000.

Frontend

Open another terminal:

cd frontend
npm install
npm run dev

Create a .env file inside the frontend directory:

VITE_API_URL=http://127.0.0.1:8000/api/v1

The frontend will run locally through Vite.

📡 Main API Endpoints
Method	Endpoint	Purpose
POST	/api/v1/documents/upload	Upload and automatically index a PDF
POST	/api/v1/chat	Ask questions about indexed documents
GET	/health	Check API health
💬 Example

Question

Who is the unit coordinator?

Answer

The unit coordinator is ABC

Source

ICTXXX Unit Study Guide – Page 1

🔒 Grounded Generation

EduRAG instructs the language model to answer using retrieved document context rather than relying on external knowledge. If sufficient information cannot be found in the uploaded documents, the system returns a fallback response instead of intentionally generating an unsupported answer.

🎯 Project Purpose

EduRAG was developed as a portfolio project to demonstrate practical implementation of:

Retrieval-Augmented Generation
Large Language Model integration
Vector databases and semantic search
Embedding-based information retrieval
REST API development
Full-stack AI application development
🔮 Future Improvements

Potential future enhancements include:

User-specific document collections
Conversation history
Hybrid search and reranking
Authentication
Persistent cloud vector storage
Streaming LLM responses
Additional document formats

👤 Author
Javeria Samreen
Software Developer | Python | FastAPI | Generative
AI | RAG
