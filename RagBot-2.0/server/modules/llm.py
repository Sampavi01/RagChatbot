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
    llm = ChatGoogleGenerativeAI(
        api_key=GEMINI_API_KEY,
        model="gemini-2.0-flash",
        temperature=0.0
    )

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
        llm=llm,
        chain_type="stuff",
        retriever=retriever,
        chain_type_kwargs={"prompt": prompt},
        return_source_documents=True
    )

