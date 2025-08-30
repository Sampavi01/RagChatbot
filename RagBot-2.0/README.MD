# 🤖✨ RagBot 2.0 - Intelligent Document Chatbot

<div align="center">

![RagBot Logo](ezgif.com-speed%20(4).gif)

**Revolutionary Retrieval-Augmented Generation Chatbot for Intelligent Document Conversations**

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-green.svg)](https://fastapi.tiangolo.com)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.25+-red.svg)](https://streamlit.io)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

</div>

---

## 🌟 What is RagBot 2.0?

RagBot 2.0 is a cutting-edge **Retrieval-Augmented Generation (RAG)** chatbot that transforms how you interact with your documents. Upload PDFs, ask questions, and receive intelligent, context-aware answers powered by advanced AI models.

### 🎯 Key Capabilities
- 📚 **Smart Document Processing** - Upload and analyze multiple PDF files
- 🧠 **AI-Powered Conversations** - Get intelligent answers using Gemini LLM
- 🔍 **Semantic Search** - Find relevant information across your documents
- 💬 **Natural Chat Interface** - Intuitive conversation flow
- 📥 **History Management** - Download and review your chat sessions

---
## 📁 Project Structure

```
RagBot-2.0/
├── 🚀 server/           # FastAPI backend with RAG engine
│   ├── main.py         # API endpoints & server logic
│   ├── modules/        # Core RAG modules
│   ├── chroma_db/      # Vector database storage
│   └── README.md       # Detailed server documentation
├── 🖥️ client/          # Streamlit frontend application
│   ├── app.py          # Main client application
│   ├── components/     # UI components
│   ├── utils/          # API utilities
│   └── README.md       # Detailed client documentation
└── 📖 README.md        # This file - Project overview
```

---

## 🔧 Technology Stack

| Component | Technology | Purpose |
|-----------|------------|---------|
| **Backend** | FastAPI + Python | High-performance API server |
| **Frontend** | Streamlit | Interactive web interface |
| **AI Engine** | LangChain | RAG pipeline orchestration |
| **Language Model** | Gemini API | Intelligent text generation |
| **Embeddings** | HuggingFace | Document vectorization |
| **Vector Database** | ChromaDB | Semantic search storage |
| **Document Processing** | PyPDF2 | PDF text extraction |

---

## 📚 Detailed Documentation

For comprehensive setup and usage instructions, please refer to:

- **[🖥️ Client Documentation](client/README.md)** - Frontend setup, UI components, and user guide
- **[🚀 Server Documentation](server/README.md)** - Backend setup, API endpoints, and technical details

---


## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.
