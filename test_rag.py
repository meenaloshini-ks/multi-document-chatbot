from dotenv import load_dotenv
from rag_chain import get_rag_chain

load_dotenv()

qa_chain = get_rag_chain()

query="How many days of privilege leave am I entitled to per year?"
result = qa_chain(query) 

print("Answer:", result["result"])
print("\nSources used:")
unique_sources = set(doc.metadata.get("source_filename") for doc in result["source_documents"])
for source in unique_sources:
    print(f"- {source}")