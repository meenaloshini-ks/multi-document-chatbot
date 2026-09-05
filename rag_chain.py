from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from vector_store import get_vector_store

PROMPT_TEMPLATE = """Answer the question using only the context below and the conversation history.
If the context doesn't contain the answer, say you don't know.

Conversation History:
{chat_history}

Context:
{context}

Question: {question}

Answer:"""

def get_rag_chain():
    vector_store = get_vector_store()
    retriever = vector_store.as_retriever(search_kwargs={"k": 3})
    llm = ChatOllama(model="llama3.2", temperature=0)
    prompt = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)

    def answer_question(query: str, chat_history: list[dict] = None):
        if chat_history is None:
            chat_history = []

        history_text = "\n".join(
            f"{turn['role']}: {turn['content']}" for turn in chat_history
        )

        retrieved_docs = retriever.invoke(query)
        context = "\n\n".join(doc.page_content for doc in retrieved_docs)

        chain = prompt | llm | StrOutputParser()
        answer = chain.invoke({
            "context": context,
            "question": query,
            "chat_history": history_text
        })

        return {
            "result": answer,
            "source_documents": retrieved_docs
        }

    return answer_question