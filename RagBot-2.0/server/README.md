# RagBot 2.0 Server

## Overview
RagBot 2.0 Server is a FastAPI-based backend for a Retrieval-Augmented Generation (RAG) chatbot. It enables document upload, vector store management, and intelligent question answering using state-of-the-art language models and embeddings.

---

## Features
- **PDF Upload**: Upload multiple PDF files for knowledge ingestion.
- **Vector Store**: Documents are embedded and stored using ChromaDB for efficient retrieval.
- **Question Answering**: Ask questions and get context-aware answers powered by Gemini and HuggingFace embeddings.
- **Robust Error Handling**: All endpoints are protected with middleware for clean error responses.
- **CORS Support**: Ready for integration with any frontend.
- **Background Processing**: Vector store updates run asynchronously for fast uploads.

---

## API Endpoints

### `POST /upload_pdfs/`
Upload one or more PDF files. Files are saved and processed in the background.
- **Request**: Multipart/form-data with files
- **Response**: JSON message indicating upload and processing status

### `POST /ask/`
Ask a question based on the uploaded documents.
- **Request**: Form data with `question` string
- **Response**: JSON answer from the RAG pipeline

### `GET /test`
Health check endpoint.
- **Response**: `{ "message": "Testing successful..." }`

---

## Technology Stack
- **FastAPI**: High-performance Python web framework
- **LangChain**: Document processing, embeddings, and LLM orchestration
- **ChromaDB**: Vector database for document retrieval
- **Gemini API**: Google Generative AI for LLM responses
- **HuggingFace Embeddings**: For semantic search and retrieval

---

## Setup & Installation

1. **Clone the repository**
   ```sh
   git clone <your-repo-url>
   cd RagBot-2.0/server
   ```
2. **Install dependencies**
   ```sh
   pip install -r requirements.txt
   ```
3. **Set environment variables**
   - `GEMINI_API_KEY`: Your Gemini API key for LLM access

4. **Run the server**
   ```sh
   uvicorn main:app --reload
   ```

---

## Folder Structure
```
server/
├── main.py              # FastAPI application
├── logger.py            # Logging setup
├── modules/             # Core modules (LLM, vectorstore, handlers)
├── requirements.txt     # Python dependencies
├── README.md            # This file
└── uploaded_pdfs/       # Uploaded documents
```

---

## Contributing
Pull requests and issues are welcome! Please follow best practices and ensure all code is well-documented.

---

## License
This project is licensed under the MIT License.

---

## Contact
For questions or support, please contact the maintainer at [your-email@example.com].
