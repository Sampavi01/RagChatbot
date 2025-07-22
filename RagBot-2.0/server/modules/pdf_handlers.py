"""
pdf_handlers.py
---------------
Utility functions for handling PDF file uploads in RagBot 2.0 server.
Provides a function to save uploaded files to disk and return their file paths.
"""

import os
import shutil
from fastapi import UploadFile
import tempfile
import sys
print("Python executable:", sys.executable)
print("Python version:", sys.version)

UPLOAD_DIR="./uploaded_pdfs"

def save_uploaded_files(files:list[UploadFile]) -> list[str] :
    """
    Save uploaded PDF files to the UPLOAD_DIR and return their file paths.

    Args:
        files (list[UploadFile]): List of FastAPI UploadFile objects.

    Returns:
        list[str]: List of file paths for the saved files.
    """
    os.makedirs(UPLOAD_DIR,exist_ok=True)
    file_paths=[]
    for file in files:
        temp_path=os.path.join(UPLOAD_DIR,file.filename)
        with open(temp_path,"wb") as f:
            shutil.copyfileobj(file.file,f)
        file_paths.append(temp_path)
    return file_paths