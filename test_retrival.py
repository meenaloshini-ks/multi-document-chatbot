from vector_store import get_vector_store

vector_store=get_vector_store()

query="How many days of privilege leave am I entitled to per year?"
results=vector_store.similarity_search(query,k=3)

for i,doc in enumerate(results):
 print(f"\n--- Result {i+1} ---")
 print(f"Source: {doc.metadata.get('source_filename')}")
 print(f"Content: {doc.page_content[:200]}")
