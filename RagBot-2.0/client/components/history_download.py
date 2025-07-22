"""
history_download.py
-------------------
Streamlit component for downloading chat history in RagBot 2.0 client.
Provides a button to export the current chat session as a text file.
"""

import streamlit as st

def render_history_download():
    """
    Render a download button for exporting chat history.

    - Checks for chat messages in session state.
    - Formats chat history as text.
    - Allows user to download the chat as a .txt file.
    """
    if st.session_state.get("message"):
        chat_text="\n\n".join([f"{m['role'].upper()}: {m['content']}" for m in st.session_state.messages])
        st.download_button("Download Chat History",chat_text,file_name="chat_history.txt",mime="text/plain")