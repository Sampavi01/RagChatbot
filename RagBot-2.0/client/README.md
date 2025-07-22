# ✨ RagBot 2.0 Client

---

## 🧠 Overview
RagBot 2.0 Client is a modern, user-friendly front-end for interacting with the RagBot 2.0 Server. Effortlessly upload documents, chat with your RAG-powered assistant, and manage your conversation history—all in one place.

---

## 🚀 Features
- **Intuitive Chat UI**: Real-time, conversational interface for seamless interactions.
- **Multi-PDF Upload**: Expand your bot's knowledge base with just a few clicks.
- **History Download**: Save and manage your chat history for future reference.
- **Robust API Integration**: Fast, reliable communication with the FastAPI backend.
- **Easy Configuration**: Adjust client settings via `config.py` for a personalized experience.

---

## 📁 Folder Structure
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

## ⚡ Setup & Installation

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
   streamlit run app.py
   ```

---

## 💡 Usage
- **Start the client**: Launch the app and interact with the chatbot.
- **Upload PDFs**: Use the upload feature to add new documents.
- **Chat**: Ask questions and receive intelligent answers.
- **Download History**: Save your chat history for later use.

---

## 🛠️ Technology Stack
- **Python**: Core programming language
- **FastAPI**: Backend API integration
- **Streamlit**: Interactive UI components
- **Custom UI Components**: Built for simplicity and extensibility

---

## 🤝 Contributing
We welcome contributions! Please submit issues and pull requests for improvements or bug fixes. Help us make RagBot even better.

---

## 📜 License
This project is licensed under the MIT License.


