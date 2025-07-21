import os
from pathlib import Path
from dotenv import load_dotenv
from tqdm.auto import tqdm
from typing import List, Optional
from pydantic import BaseModel
from typing_extensions import TypedDict

from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain_core.documents import Document

load_dotenv()

UPLOAD_DIR = "./uploaded_pdfs"
CHROMA_DIR = "./chroma_db"
os.makedirs(UPLOAD_DIR, exist_ok=True)

class DocumentModel(BaseModel):
    id: str
    title: str
    description: Optional[str] = None
    createdAt: str
    fileSize: int
    pages: int
    contents: List[str]

class QueryRequest(BaseModel):
    document: DocumentModel
    query: str

class Source(BaseModel):
    text: str
    page: int

class QueryResponse(BaseModel):
    answer: str
    sources: List[Source]

class State(TypedDict):
    question: str
    context: List[Document]
    answer: str

def split_document(document: DocumentModel):
    docs = [
        Document(page_content=content, metadata={"page": i+1})
        for i, content in enumerate(document.contents)
    ]
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
        add_start_index=True,
    )
    all_splits = text_splitter.split_documents(docs)
    return all_splits

async def get_sources(vector_store, query: str, max_sources: int = 3) -> List[Source]:
    retrieved_docs = vector_store.similarity_search(query, k=max_sources)
    sources = []
    for doc in retrieved_docs:
        page = doc.metadata.get("page", 0)
        sources.append(Source(
            text=doc.page_content[:200] + ("..." if len(doc.page_content) > 200 else ""),
            page=page
        ))
    return sources

def load_vectorstore(uploaded_files):
    hf_embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

    all_chunks = []
    for file_path in uploaded_files:
        loader = PyPDFLoader(file_path)
        documents = loader.load()
        print(f"Loaded {len(documents)} docs from {file_path}")
        for doc in documents[:3]:
            print(f"Doc preview: {doc.page_content[:100]}")

        splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
        chunks = splitter.split_documents(documents)

        all_chunks.extend(chunks)

    print(f"Total chunks to embed: {len(all_chunks)}")
    if len(all_chunks) == 0:
        print("Warning: No document chunks found! Embeddings will be empty.")

    vector_store = Chroma(
        collection_name="my_docs",
        embedding_function=hf_embedding_model,
        persist_directory=CHROMA_DIR
    )

    vector_store.add_documents(all_chunks)
    

    print("✅ ChromaDB update complete.")
    return vector_store


def retrieve(vector_store, state: State):
    retrieved_docs = vector_store.similarity_search(state["question"])
    return {"context": retrieved_docs}

def generate(prompt, llm, state: State):
    docs_content = "\n\n".join(doc.page_content for doc in state["context"])
    messages = prompt.invoke({"question": state["question"], "context": docs_content})
    response = llm.invoke(messages)
    return {"answer": response.content}

