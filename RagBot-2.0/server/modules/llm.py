"""
llm.py
--------
Provides a function to build a Retrieval-Augmented Generation (RAG) chain using LangChain and Gemini LLM.
Loads the Gemini API key from environment variables and constructs a QA chain with a custom prompt template.
"""
from langchain.prompts import PromptTemplate
from langchain.chains import RetrievalQA
from langchain_google_genai import ChatGoogleGenerativeAI
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Use GEMINI_API_KEY instead of GOOGLE_API_KEY
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

def get_llm_chain(retriever, llm):
    """
    Build a RetrievalQA chain using LangChain and Gemini LLM.

    Args:
        retriever: LangChain retriever object for document retrieval.
        llm: Gemini LLM instance (not used, will be overwritten).

    Returns:
        RetrievalQA: LangChain RetrievalQA chain configured with Gemini LLM and a custom prompt.
    """
    # ✅ FIXED PromptTemplate
    prompt = PromptTemplate(
        input_variables=["context", "question"],
        template="""
You are a helpful AI assistant. Answer the user's question based only on the following context.

If the answer is not contained within the text provided, say: "I could not find the answer in the provided documents."
Do not make up information.

Context:
{context}

Question: 
{question}
"""
    )

    return RetrievalQA.from_chain_type(
        llm=llm,                                  # LLM to generate answers
        chain_type="stuff",                       # Stuff all context together into one input
        retriever=retriever,                      # Use this retriever to fetch relevant chunks
        chain_type_kwargs={"prompt": prompt},     # Use the custom prompt defined above
        return_source_documents=True              # Also return which documents the answer came from
    )

