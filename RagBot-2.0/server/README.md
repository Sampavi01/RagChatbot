# 🚀 RagBot 2.0 Server

---

## 🧠 Overview
RagBot 2.0 Server is a robust FastAPI backend for Retrieval-Augmented Generation (RAG) chatbots. It empowers users to upload documents, manage a vector store, and receive intelligent, context-aware answers using cutting-edge language models and embeddings.

---

## ✨ Features
- **Seamless PDF Uploads**: Effortlessly ingest multiple PDF files to expand your knowledge base.
- **Advanced Vector Store**: Documents are embedded and indexed using ChromaDB for lightning-fast retrieval.
- **Smart Question Answering**: Get precise, context-driven answers powered by Gemini LLM and HuggingFace embeddings.
- **Resilient Error Handling**: Middleware ensures clean, informative error responses for all endpoints.
- **Universal CORS Support**: Integrate with any frontend, anywhere.
- **Efficient Background Processing**: Vector store updates run asynchronously for a smooth user experience.

---

## 🔗 API Endpoints

### `POST /upload_pdfs/`
Upload one or more PDF files. Files are saved and processed in the background.
- **Request**: `multipart/form-data` with files
- **Response**: JSON message indicating upload and processing status

### `POST /ask/`
Ask a question based on the uploaded documents.
- **Request**: Form data with `question` string
- **Response**: JSON answer from the RAG pipeline

### `GET /test`
Health check endpoint.
- **Response**: `{ "message": "Testing successful..." }`

---

## 🛠️ Technology Stack
- **FastAPI**: High-performance Python web framework
- **LangChain**: Document processing, embeddings, and LLM orchestration
- **ChromaDB**: Vector database for document retrieval
- **Gemini API**: Google Generative AI for LLM responses
- **HuggingFace Embeddings**: For semantic search and retrieval

---

## ⚡ Quickstart

1. **Clone the repository**
   ```sh
   git clone <https://github.com/Sampavi01/RagChatbot.git>
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

## 📁 Folder Structure
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

## 🤝 Contributing
We welcome pull requests and issues! Please follow best practices and ensure all code is well-documented. Your contributions help make RagBot better for everyone.

---

## 📜 License
This project is licensed under the MIT License.

.
