# RagBot 2.0 Client

## Overview
RagBot 2.0 Client is the front-end and utility layer for interacting with the RagBot 2.0 Server. It provides a user-friendly interface for uploading documents, chatting with the RAG-powered bot, and managing conversation history.

---

## Features
- **Chat UI**: Modern interface for real-time conversations with the RAG chatbot.
- **PDF Upload**: Upload documents to expand the bot's knowledge base.
- **Conversation History**: Download and manage chat history for future reference.
- **API Integration**: Seamless communication with the FastAPI backend.
- **Configurable Settings**: Easily adjust client parameters via `config.py`.

---

## Folder Structure
```
client/
├── app.py                # Main application entry point
├── config.py             # Client configuration
├── requirements.txt      # Python dependencies
├── README.md             # This file
├── components/           # UI and utility components
│   ├── chatUI.py         # Chat interface logic
│   ├── history_download.py # Download chat history
│   └── upload.py         # File upload logic
└── utils/                # API utilities
    └── api.py            # API request handling
```

---

## Setup & Installation

1. **Navigate to the client directory**
   ```sh
   cd RagBot-2.0/client
   ```
2. **Install dependencies**
   ```sh
   pip install -r requirements.txt
   ```
3. **Configure client settings**
   - Edit `config.py` to set API endpoints and other parameters as needed.

4. **Run the client application**
   ```sh
   python app.py
   ```

---

## Usage
- **Start the client**: Launch the app and interact with the chatbot.
- **Upload PDFs**: Use the upload feature to add new documents.
- **Chat**: Ask questions and receive intelligent answers.
- **Download History**: Save your chat history for later use.

---

## Technology Stack
- **Python**: Core programming language
- **FastAPI**: Backend API integration
- **Custom UI Components**: Built with Python for simplicity and extensibility

---

## Contributing
Contributions are welcome! Please submit issues and pull requests for improvements or bug fixes.

---

## License
This project is licensed under the MIT License.

---

## Contact
For support or questions, contact the maintainer at [your-email@example.com].
