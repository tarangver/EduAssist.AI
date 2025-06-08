# EduAssist AI: Chatbot with Groq + Streamlit

EduAssist AI is an academic assistant chatbot powered by LLMs from Groq and deployed using Streamlit.

## 🚀 Features
- Chat interface built with Streamlit
- LLM models served via Groq API (LLaMA3, Mixtral, Gemma)
- `.env` file for secure API key management

## 📦 Tools Used
- Streamlit
- Groq API (https://console.groq.com)
- Python
## 📁 How to Run

1. Clone the repository:
```bash
git clone https://github.com/your-username/eduassist-chatbot.git
cd eduassist-chatbot
```

2. Create `.env` file and add your Groq API key:
```
GROQ_API_KEY=sk-your-real-api-key-here
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the app:
```bash
streamlit run app.py
```

## 🌐 Deploy to Streamlit Cloud

- Upload the project to GitHub
- On [Streamlit Cloud](https://share.streamlit.io), create a new app from the repo
- In "Secrets", add your `GROQ_API_KEY` if not using `.env`

## 📸 UI Preview

Dark-themed chatbot interface with model selection.

<img src="https://github.com/tarangver/EduAssist.AI/raw/main/chatBot.png" alt="Chatbot UI Preview" width="650"/>

Made with ❤️ by TARNG VERMA
