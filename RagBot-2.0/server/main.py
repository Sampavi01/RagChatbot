"""
main.py
-------
FastAPI application for RagBot 2.0 server.
Handles PDF uploads, vector store management, and question answering using LangChain, ChromaDB, HuggingFace embeddings, and Gemini LLM.

Endpoints:
    - POST /upload_pdfs/: Upload and process PDF files asynchronously.
    - POST /ask/: Ask questions based on uploaded documents.
    - GET /test: Health check endpoint.

Constants:
    - UPLOAD_DIR: Directory for uploaded PDFs.
    - PERSIST_DIR: Directory for ChromaDB persistence.
    - COLLECTION_NAME: ChromaDB collection name.
"""

from fastapi import FastAPI, UploadFile, File, Form, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi import BackgroundTasks
from typing import List
from modules.load_vectorstore import load_vectorstore
from modules.llm import get_llm_chain
from modules.query_handlers import query_chain
from logger import logger
from pathlib import Path  
import os

# Use the recommended, non-deprecated Chroma class
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_google_genai import ChatGoogleGenerativeAI

# --- Define Constants in ONE place to ensure consistency ---
UPLOAD_DIR = Path("./uploaded_pdfs")
PERSIST_DIR = Path("./chroma_db")  # This MUST match the directory in load_vectorstore
COLLECTION_NAME = "my_docs"     # This MUST match the collection in load_vectorstore

# Create directories if they don't exist
UPLOAD_DIR.mkdir(exist_ok=True)
PERSIST_DIR.mkdir(exist_ok=True)

app = FastAPI(title="RagBot2.0")

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.middleware("http")
async def catch_exception_middleware(request: Request, call_next):
    try:
        return await call_next(request)
    except Exception as exc:
        logger.exception("UNHANDLED EXCEPTION")
        return JSONResponse(status_code=500, content={"error": str(exc)})

@app.post("/upload_pdfs/")
async def upload_pdfs(
    files: List[UploadFile] = File(...),
    background_tasks: BackgroundTasks = BackgroundTasks()
):
    try:
        logger.info(f"Received {len(files)} files")

        saved_files = []
        for file in files:
            contents = await file.read()
            safe_filename = Path(file.filename).name
            if not safe_filename:
                raise ValueError("Empty filename received")

            save_path = UPLOAD_DIR / safe_filename
            with open(save_path, "wb") as f:
                f.write(contents)
            saved_files.append(str(save_path))

        # Run load_vectorstore as background task
        background_tasks.add_task(load_vectorstore, saved_files)

        logger.info("Vectorstore loading scheduled in background")
        return {"message": "Files uploaded. Vectorstore update is running in background."}

    except Exception as e:
        logger.exception("Error during PDF upload")
        return JSONResponse(status_code=500, content={"error": str(e)})

# --- CORRECTED AND REFACTORED /ask/ ENDPOINT ---
@app.post("/ask/")
async def ask_question(question: str = Form(...)):
    try:
        logger.info(f"User query: {question}")

        # 1. Initialize the embedding model with the same stable configuration
        embedding_model = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2",
            model_kwargs={'device': 'cpu'}  # Added for stability and consistency
        )

        # 2. Load the vector store using the CORRECT directory and collection name
        vectorstore = Chroma(
            persist_directory=str(PERSIST_DIR),         
            embedding_function=embedding_model,
            collection_name=COLLECTION_NAME             
        )

        # Create Gemini API LLM instance with clean indentation
        llm = ChatGoogleGenerativeAI(
            api_key=os.getenv("GEMINI_API_KEY"),
            model="gemini-1.5-flash"  # Corrected to a valid model name
        )

        # Get LangChain retriever from vectorstore
        retriever = vectorstore.as_retriever(search_kwargs={"k": 5}) # Retrieve top 5 chunks

        # Get your LLM + retrieval QA chain
        # Make sure get_llm_chain is compatible with this setup
        chain = get_llm_chain(retriever, llm) 

        # Query the chain
        result = query_chain(chain, question)

        logger.info("Query successful")
        return result

    except Exception as e:
        logger.exception("Error processing question")
        return JSONResponse(status_code=500, content={"error": str(e)})

@app.get("/test")
async def test():
    return {"message": "Testing successful..."}