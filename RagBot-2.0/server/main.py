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

from langchain_community.vectorstores import Chroma

from langchain_core.documents import Document
from langchain_huggingface import HuggingFaceEmbeddings


from langchain_google_genai import ChatGoogleGenerativeAI  # Gemini API LLM
UPLOAD_DIR = "./uploaded_pdfs"
os.makedirs(UPLOAD_DIR, exist_ok=True)


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

            save_path = Path(UPLOAD_DIR) / safe_filename
            with open(save_path, "wb") as f:
                f.write(contents)
            saved_files.append(save_path)

        # 🔄 Run load_vectorstore as background task
        background_tasks.add_task(load_vectorstore, [str(f) for f in saved_files])

        logger.info("Vectorstore loading scheduled in background")
        return {"message": "Files uploaded. Vectorstore update is running in background."}

    except Exception as e:
        logger.exception("Error during PDF upload")
        return JSONResponse(status_code=500, content={"error": str(e)})

@app.post("/ask/")
async def ask_question(question: str = Form(...)):
    try:
        logger.info(f"user query: {question}")

        # Load Chroma vectorstore from persistent directory
        PERSIST_DIR = "chroma_persist"  # adjust if needed

        embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")


        vectorstore = Chroma(
            persist_directory=PERSIST_DIR,
            embedding_function=embedding_model,
            collection_name="ragbot_collection"  # change as appropriate
        )

        # Create Gemini API LLM instance
        llm = ChatGoogleGenerativeAI(
            
    api_key=os.getenv("GEMINI_API_KEY"),  # Make sure your env var is GOOGLE_API_KEY or change accordingly
    model="gemini-2.0-flash"
)

        

        # Get LangChain retriever from vectorstore
        retriever = vectorstore.as_retriever()

        # Get your LLM + retrieval QA chain
        chain = get_llm_chain(retriever)  # update your get_llm_chain to accept llm param if not done yet

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
