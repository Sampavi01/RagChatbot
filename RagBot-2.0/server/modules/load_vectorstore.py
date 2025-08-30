"""
load_vectorstore.py
-------------------
Process uploaded PDFs, split into text chunks, clean data, and store in Chroma vector database.
"""

from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from typing import List
import torch
import os

CHROMA_DIR = "./chroma_db"

def load_vectorstore(uploaded_files: List[str]):
    """
    Loads PDF documents, splits into text chunks, cleans chunks, and adds to Chroma vector store.

    Args:
        uploaded_files (List[str]): List of file paths to uploaded PDF documents.

    Returns:
        Chroma: Chroma vector store with embedded document chunks, or None if no valid chunks found.
    """

    # --- 1. INITIALIZE THE EMBEDDING MODEL SAFELY ON CPU ---
    device = "cpu"
    embedding_model = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2",
        model_kwargs={
            "device": device,
            "torch_dtype": torch.float32,
            "low_cpu_mem_usage": True
        }
    )

    # --- 2. LOAD AND SPLIT ALL DOCUMENTS ---
    all_chunks = []
    for file_path in uploaded_files:
        try:
            print(f"Processing file: {file_path}")
            loader = PyPDFLoader(file_path)
            documents = loader.load()
            print(f"Loaded {len(documents)} pages from {file_path}")

            splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
            chunks = splitter.split_documents(documents)
            all_chunks.extend(chunks)
        except Exception as e:
            print(f"Error processing {file_path}: {e}. Skipping this file.")
            continue

    # --- 3. CLEAN THE COLLECTED CHUNKS ---
    if not all_chunks:
        print("Warning: No chunks generated from uploaded files.")
        return None

    cleaned_chunks = [
        doc for doc in all_chunks if isinstance(doc.page_content, str) and len(doc.page_content.strip()) > 0
    ]

    if not cleaned_chunks:
        print("Warning: No valid text chunks after cleaning. ChromaDB not updated.")
        return None

    print(f"Total valid chunks to embed after cleaning: {len(cleaned_chunks)}")

    # --- 4. INITIALIZE OR LOAD THE VECTOR STORE ---
    os.makedirs(CHROMA_DIR, exist_ok=True)
    vector_store = Chroma(
        collection_name="my_docs",
        embedding_function=embedding_model,
        persist_directory=CHROMA_DIR
    )

    # Add only cleaned chunks to Chroma
    vector_store.add_documents(cleaned_chunks)
    vector_store.persist()  # persist changes to disk

    print("✅ ChromaDB update complete.")
    return vector_store

     