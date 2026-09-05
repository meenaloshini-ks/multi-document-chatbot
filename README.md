# Multi-Document RAG Chatbot

A Retrieval-Augmented Generation (RAG) application that allows users to ask questions about multiple documents and receive context-based answers.

The project uses a **FastAPI backend**, a **Streamlit chat interface**, **ChromaDB** for vector storage, and the **OpenAI API** for answer generation.

## Features

* Loads and processes multiple documents
* Splits document text into manageable chunks
* Converts text chunks into embeddings
* Stores and retrieves embeddings using ChromaDB
* Performs semantic similarity search
* Generates answers using relevant document context
* FastAPI-based backend
* Interactive Streamlit chat interface
* Keeps API keys and local documents out of GitHub

## Project Workflow

1. Documents are loaded and their text is extracted.
2. The extracted text is divided into smaller chunks.
3. Embeddings are created for each chunk.
4. Embeddings are stored in ChromaDB.
5. The user's question is converted into an embedding.
6. The most relevant document chunks are retrieved.
7. The retrieved context is sent to the language model.
8. The generated answer is displayed in the Streamlit interface.

## Project Structure

```text
multi-document-chatbot/
├── chat_ui.py             # Streamlit user interface
├── main.py                # FastAPI application
├── document_loader.py     # Document loading and text extraction
├── chunker.py             # Text chunking
├── vector_store.py        # ChromaDB vector storage and retrieval
├── rag_chain.py           # Retrieval and answer-generation pipeline
├── test_loader.py         # Document-loader tests
├── test_rag.py            # RAG pipeline tests
├── test_retrival.py       # Retrieval tests
├── requirements.txt       # Python dependencies
├── .gitignore             # Files excluded from Git
└── README.md              # Project documentation
```

## Technologies Used

* Python
* FastAPI
* Streamlit
* OpenAI API
* ChromaDB
* LangChain
* Vector embeddings
* Retrieval-Augmented Generation
* Semantic search

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/meenaloshini-ks/multi-document-chatbot.git
cd multi-document-chatbot
```

### 2. Create a virtual environment

Windows:

```powershell
python -m venv venv
venv\Scripts\activate
```

macOS/Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install the dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure the API key

Create a `.env` file in the project directory:

```env
OPENAI_API_KEY=your_openai_api_key
```

Never commit the `.env` file or share the API key publicly.

## Running the Application

### Start the FastAPI backend

Open a terminal and run:

```bash
uvicorn main:app --reload
```

The API will normally be available at:

```text
http://127.0.0.1:8000
```

FastAPI documentation can be viewed at:

```text
http://127.0.0.1:8000/docs
```

### Start the Streamlit interface

Keep the FastAPI terminal running. Open another terminal, activate the virtual environment, and run:

```bash
streamlit run chat_ui.py
```

Streamlit will open the chatbot interface in your browser.

## Local Data

Local documents, generated embeddings, ChromaDB files, virtual environments, cache files, and environment variables are excluded from GitHub through `.gitignore`.

Add the required documents locally before running the document-processing pipeline.

## Security

* API keys are stored only in `.env`.
* `.env` is excluded from version control.
* Local documents are not uploaded to the repository.
* Generated vector database files are not committed.

## Future Improvements

* Add support for more document formats
* Display document sources with every answer
* Add conversation history
* Improve error handling and validation
* Add authentication
* Deploy the frontend and backend online
* Add automated tests and CI/CD

## Author

**Meenaloshini K S**

GitHub: [meenaloshini-ks](https://github.com/meenaloshini-ks)

## Repository

[Multi-Document RAG Chatbot](https://github.com/meenaloshini-ks/multi-document-chatbot)
