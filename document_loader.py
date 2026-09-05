import os
from langchain_community.document_loaders import PyPDFLoader, TextLoader
from langchain_core.documents import Document

def load_document(file_path: str) -> list[Document]:
    if file_path.endswith(".pdf"):
        loader = PyPDFLoader(file_path)
    elif file_path.endswith(".txt"):
        loader = TextLoader(file_path,encoding="utf-8")
    else:
        raise ValueError(f"Unsupported file type: {file_path}")

    docs = loader.load()

    for doc in docs:
        doc.metadata["source_filename"] = os.path.basename(file_path)

    return docs