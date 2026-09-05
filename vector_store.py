from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain_core.documents import Document

PERSIST_DIRECTORY = "chroma_db"

def get_vector_store():
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vector_store = Chroma(
        persist_directory=PERSIST_DIRECTORY,
        embedding_function=embeddings
    )
    return vector_store

def add_documents_to_store(chunks: list[Document]):
    vector_store = get_vector_store()
    vector_store.add_documents(chunks)
    return vector_store