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

model_map = {
    # Existing models
    "Google Gemma 2 9B": "gemma2-9b-it",
    "Meta LLaMA 3 8B": "llama3-8b-8192",
    "Meta LLaMA 3 70B": "llama3-70b-8192",
    # Additional models
    "LLaMA 3.1 8B (instant)": "llama-3.1-8b-instant",
    "LLaMA 3.1 70B Versatile": "llama-3.1-70b-versatile",
    "LLaMA 3.2 1B (preview)": "llama-3.2-1b-preview",
    "LLaMA 3.2 3B (preview)": "llama-3.2-3b-preview",
    "LLaMA 3.2 11B (preview)": "llama-3.2-11b-text-preview",
    "LLaMA 3.2 90B (preview)": "llama-3.2-90b-text-preview",
    "LLaMA 3.3 70B (versatile)": "llama-3.3-70b-versatile",
    "Mixtral 8B 32K": "mixtral-8x7b-32768",
    "Deepseek R1 Distill 70B": "deepseek-r1-distill-llama-70b",
    "LLaMA 4 Maverick 17B": "groq:meta-llama/llama-4-maverick-17b-128e-instruct",
    "LLaMA 4 Scout 17B": "groq:meta-llama/llama-4-scout-17b-16e-instruct",
    "Gemma 7B (deprecated)": "gemma-7b-it",
    "Distil Whisper (ASR)": "distil-whisper-large-v3-en",
    "LLaVA v1.5 7B Multimodal": "LLaVA-v1.5-7b-preview"
}

selected_label = st.sidebar.selectbox("Choose a model", list(model_map.keys()))
model = model_map[selected_label]

st.sidebar.markdown("---")
st.sidebar.caption("Powered by [Groq](https://groq.com) & Streamlit")

st.sidebar.markdown("Made with ❤️ by **TARNG VERMA**", unsafe_allow_html=True)
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


