"""
query_handlers.py
-----------------
Provides utility functions for querying the RAG chain and formatting responses for RagBot 2.0 server.
"""

from logger import logger

def query_chain(chain, user_input: str):
    """
    Run the RAG chain with the given user input and format the response.

    Args:
        chain: The LangChain QA chain to execute.
        user_input (str): The user's question or query string.

    Returns:
        dict: A dictionary with the answer ('response') and a list of document sources ('sources').

    Raises:
        Exception: Logs and re-raises any error encountered during chain execution.
    """
    try:
        logger.debug(f"Running chain for input: {user_input}")
        result=chain({"query":user_input})
        response={
            "response":result["result"],
            "sources":[doc.metadata.get("source","") for doc in result["source_documents"]]
        }
        logger.debug(f"Chain response: {response}")
        return response
    except Exception as e:
        logger.exception("Error in query_chain")
        raise