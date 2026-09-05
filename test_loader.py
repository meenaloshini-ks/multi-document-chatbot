import os
from dotenv import load_dotenv
from document_loader import load_document
from chunker import chunk_documents
from vector_store import add_documents_to_store

load_dotenv()

data_folders = ["data/pdf", "data/text"]
all_chunks=[]

for folder in data_folders:
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        documents = load_document(file_path)
        chunks=chunk_documents(documents)
        all_chunks.extend(chunks)
        print(f"{filename} : {len(chunks)} chunks")

print(f"\nTotal chunks to store: {len(all_chunks)}")
add_documents_to_store(all_chunks)
print("All chunks embedded and stored in Chroma!")
      