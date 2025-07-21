import requests
from config import API_URL

def upload_pdfs_api(files):
    try:
        files_payload = [("files", (f.name, f.read(), "application/pdf")) for f in files]

        response = requests.post(
            f"{API_URL}/upload_pdfs/",
            files=files_payload,
            timeout=60,       # Increase timeout in case it's a big file
            stream=False      # Avoid streaming broken response
        )

        response.raise_for_status()  # Raises HTTPError for bad status codes
        return response
    except requests.exceptions.RequestException as e:
        print("❌ Upload failed:", e)
        return None

    

def ask_question(question):
    return requests.post(f"{API_URL}/ask/",data={"question":question})