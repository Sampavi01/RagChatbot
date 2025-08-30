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
    # Create the upload directory if it doesn't exist already
    os.makedirs(UPLOAD_DIR,exist_ok=True)

    # This list will store the paths of all successfully saved files
    file_paths=[]

    # Iterate over each uploaded file
    for file in files:
        # Generate the full path where this file will be saved
        temp_path=os.path.join(UPLOAD_DIR,file.filename)
        # Open the destination file in write-binary mode
        with open(temp_path,"wb") as f:
            # Copy the contents of the uploaded file to the destination file
            shutil.copyfileobj(file.file,f)
        file_paths.append(temp_path)               # Add the saved file's path to the list
    
    return file_paths                              # Return the list of saved file paths