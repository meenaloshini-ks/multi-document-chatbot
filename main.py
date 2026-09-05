from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel
import shutil
from document_loader import load_document
from chunker import chunk_documents
from vector_store import add_documents_to_store
from rag_chain import get_rag_chain

app = FastAPI()

qa_chain = get_rag_chain() 


class ChatRequest(BaseModel):
    query: str
    session_id: str = "default"

conversation_store: dict[str, list[dict]] = {}

@app.post("/chat")
async def chat(request: ChatRequest):
    history = conversation_store.get(request.session_id, [])

    result = qa_chain(request.query, chat_history=history)

    history.append({"role": "user", "content": request.query})
    history.append({"role": "assistant", "content": result["result"]})
    conversation_store[request.session_id] = history

    sources = list(set(doc.metadata.get("source_filename") for doc in result["source_documents"]))

    return {
        "answer": result["result"],
        "sources": sources
    }