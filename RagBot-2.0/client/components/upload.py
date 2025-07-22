"""
upload.py
---------
Streamlit component for uploading PDF documents in RagBot 2.0 client.
Provides a sidebar uploader and handles API calls to the backend for document ingestion.
"""

import streamlit as st
from utils.api import upload_pdfs_api

def render_uploader():
    """
    Render the sidebar PDF uploader and handle upload logic.

    - Allows users to select and upload multiple PDF files.
    - Calls the backend API to ingest documents.
    - Displays upload status and error messages in the sidebar.
    """

    st.sidebar.header("Upload PDFs")
    uploaded_files = st.sidebar.file_uploader(
        "Upload multiple PDFs", type="pdf", accept_multiple_files=True
    )

    if st.sidebar.button("Upload to DB") and uploaded_files:
        with st.spinner("Uploading..."):
            try:
                response = upload_pdfs_api(uploaded_files)

                if response is None:
                    st.sidebar.error("Connection failed. Please try again.")
                elif response.status_code == 200:
                    st.sidebar.success("Uploaded successfully")
                else:
                    st.sidebar.error(f"❌ Error: {response.status_code} - {response.text}")

            except Exception as e:
                st.sidebar.error(f"💥 Upload crashed: {str(e)}")
