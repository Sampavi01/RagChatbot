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
        logger.debug(f"Running chain for input: {user_input}")          #Logs a debug message to indicate that the RAG chain is about to run with the user's input.
        result=chain({"query":user_input})                              # Executes the chain with the user's query, which returns a dictionary containing the answer and source documents.
        response={
            "response":result["result"],
            "sources":[doc.metadata.get("source","") for doc in result["source_documents"]]
        }
        logger.debug(f"Chain response: {response}")                    # Logs the response from the chain, which includes the answer and sources.
        return response                                                # Returns the formatted response dictionary containing the answer and sources.
    except Exception as e:
        logger.exception("Error in query_chain")                       # Logs any exception that occurs during the execution of the chain.
        raise                                                          # Re-raises the exception after logging it, allowing the caller to handle it as needed.