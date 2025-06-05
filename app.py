# ------------------- IMPORTS -------------------
import streamlit as st
import requests
from dotenv import load_dotenv
import os

# ------------------- CONFIG -------------------
st.set_page_config(page_title="EduAssist AI 🤖", layout="wide")

# Load environment variables from .env file
load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"

# ------------------- FUNCTIONS -------------------
def query_groq(messages, model="llama3-8b-8192"):
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": model,
        "messages": messages
    }

    response = requests.post(GROQ_API_URL, headers=headers, json=payload)

    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        return f"❌ Error: {response.status_code} - {response.text}"

# ------------------- SIDEBAR -------------------
st.sidebar.title("🛠️ Settings")
model = st.sidebar.selectbox("Choose a model", [
    "Google GEMMA",
    "META LLAMA 3",
    "META LLAMA 3.1",
    "META LLAMA 3.2",
    "META LLAMA 3.3"
], index=0)

st.sidebar.markdown("---")
st.sidebar.caption("Powered by [Groq](https://groq.com) & Streamlit")

# ------------------- CHAT INITIALIZATION -------------------
if "chat_history" not in st.session_state:
    st.session_state.chat_history = [
        {"role": "system", "content": "You are EduAssist AI, a helpful academic assistant for students and teachers."}
    ]

# ------------------- CHAT UI -------------------
st.title("📚 EduAssist AI")

for message in st.session_state.chat_history[1:]:  # Skip system prompt
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

user_input = st.chat_input("Ask your question...")

if user_input:
    # Add user message
    st.chat_message("user").markdown(user_input)
    st.session_state.chat_history.append({"role": "user", "content": user_input})

    # Get response from Groq
    with st.spinner("Thinking..."):
        response = query_groq(st.session_state.chat_history, model=model)

    st.chat_message("assistant").markdown(response)
    st.session_state.chat_history.append({"role": "assistant", "content": response})

# ------------------- FOOTER -------------------
st.markdown("---")
st.markdown(
    """
    Made with ❤️ by TARNG VERMA
    """
)
# ------------------- END OF FILE -------------------


