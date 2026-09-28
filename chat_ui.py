import streamlit as st
import requests

st.set_page_config(page_title="Multi-Document ChatBot", page_icon="📄")
st.title("📄 Multi-Document ChatBot")

API_URL = "http://127.0.0.1:8000"

if "messages" not in st.session_state:
    st.session_state.messages = []

if "session_id" not in st.session_state:
    st.session_state.session_id = "streamlit-session-1"

with st.sidebar:
    st.header("Upload Documents")
    uploaded_file = st.file_uploader(
        "Choose a PDF or TXT file",
        type=["pdf", "txt"]
    )

    if uploaded_file is not None and st.button("Upload"):
        try:
            files = {"file": (uploaded_file.name, uploaded_file.getvalue())}
            response = requests.post(
                f"{API_URL}/upload",
                files=files,
                timeout=60
            )

            if response.status_code == 200:
                st.success(f"Uploaded: {uploaded_file.name}")
            else:
                st.error(
                    f"Upload failed ({response.status_code}): {response.text}"
                )
        except requests.RequestException as error:
            st.error(f"Could not connect to backend: {error}")

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

user_input = st.chat_input("Ask a question about your documents...")

if user_input:
    st.session_state.messages.append(
        {"role": "user", "content": user_input}
    )

    with st.chat_message("user"):
        st.markdown(user_input)

    answer = "No answer received."

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                response = requests.post(
                    f"{API_URL}/chat",
                    json={
                        "query": user_input,
                        "session_id": st.session_state.session_id
                    },
                    timeout=60
                )

                if response.status_code == 200:
                    data = response.json()
                    answer = data.get("answer", "No answer returned.")
                    sources = data.get("sources", [])

                    st.markdown(answer)

                    if sources:
                        st.caption(f"Sources: {', '.join(sources)}")
                else:
                    answer = (
                        f"Backend error ({response.status_code}): "
                        f"{response.text}"
                    )
                    st.error(answer)

            except requests.RequestException as error:
                answer = f"Could not connect to backend: {error}"
                st.error(answer)

    st.session_state.messages.append(
        {"role": "assistant", "content": answer}
    )