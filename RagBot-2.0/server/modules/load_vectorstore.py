import os
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from typing import List

CHROMA_DIR = "./chroma_db"

def load_vectorstore(uploaded_files: List[str]):
    """
    Loads documents, splits them into chunks, cleans them, and adds them to a Chroma vector store.
    """
    # --- 1. INITIALIZE THE EMBEDDING MODEL (Correctly done) ---
    # This prevents the "meta tensor" error by specifying the device.
    model_kwargs = {'device': 'cpu'}
    hf_embedding_model = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2",
        model_kwargs=model_kwargs
    )
    
    # --- 2. LOAD AND SPLIT ALL DOCUMENTS ---
    # This list will accumulate chunks from all processed PDF files.
    all_chunks = []
    for file_path in uploaded_files:
        # The try...except block wraps each file's processing.
        # This makes the function robust; it won't crash if one PDF is bad.
        try:
            print(f"Processing file: {file_path}")
            loader = PyPDFLoader(file_path)
            documents = loader.load()
            
            print(f"Loaded {len(documents)} pages from {file_path}")

            splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
            chunks = splitter.split_documents(documents)
            all_chunks.extend(chunks)
        except Exception as e:
            print(f"Error processing file {file_path}: {e}. Skipping this file.")
            continue # This correctly skips to the next file in the loop.

    # --- 3. CLEAN THE COLLECTED CHUNKS ---
    # This step is performed *after* all chunks have been collected.
    # It removes any documents with empty or invalid content to prevent TypeErrors.
    if not all_chunks:
        print("Warning: No chunks were generated from the uploaded files.")
        return None

    cleaned_chunks = [
        doc for doc in all_chunks if isinstance(doc.page_content, str) and len(doc.page_content.strip()) > 0
    ]

    if not cleaned_chunks:
        print("Warning: No valid text chunks found after cleaning. ChromaDB will not be updated.")
        return None

    print(f"Total valid chunks to embed after cleaning: {len(cleaned_chunks)}")

    # --- 4. INITIALIZE AND POPULATE THE VECTOR STORE ---
    # The Chroma vector store is created only after we have valid chunks to add.
    vector_store = Chroma(
        collection_name="my_docs",
        embedding_function=hf_embedding_model,
        persist_directory=CHROMA_DIR
    )

    # Add only the cleaned, valid documents to the vector store.
    vector_store.add_documents(cleaned_chunks)

    print("✅ ChromaDB update complete.")
    return vector_store