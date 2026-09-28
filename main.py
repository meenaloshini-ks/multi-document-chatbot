import os
import shutil

from dotenv import load_dotenv
from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from document_loader import load_document
from chunker import chunk_documents
from vector_store import add_documents_to_store
from rag_chain import get_rag_chain

load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

UPLOAD_DIR = "data"
os.makedirs(UPLOAD_DIR, exist_ok=True)

qa_chain = get_rag_chain()
conversation_store: dict[str, list[dict]] = {}


class ChatRequest(BaseModel):
    query: str
    session_id: str = "default"


@app.post("/upload")
async def upload_document(file: UploadFile = File(...)):
    if not file.filename.endswith((".pdf", ".txt")):
        raise HTTPException(status_code=400, detail="Only PDF and TXT files are allowed.")

    file_path = os.path.join(UPLOAD_DIR, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    documents = load_document(file_path)
    chunks = chunk_documents(documents)
    add_documents_to_store(chunks)

    return {
        "message": "Document uploaded successfully",
        "filename": file.filename,
        "chunks_created": len(chunks)
    }


@app.post("/chat")
async def chat(request: ChatRequest):
    history = conversation_store.get(request.session_id, [])

    result = qa_chain(request.query, chat_history=history)

    history.append({"role": "user", "content": request.query})
    history.append({"role": "assistant", "content": result["result"]})
    conversation_store[request.session_id] = history

    sources = list({
        doc.metadata.get("source_filename")
        for doc in result["source_documents"]
        if doc.metadata.get("source_filename")
    })

    return {
        "answer": result["result"],
        "sources": sources
    }