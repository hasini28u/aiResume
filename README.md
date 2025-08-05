# AI Resume Screener & Interview Assistant

A Streamlit-based LLM application that evaluates resumes against job descriptions using Groq’s LLaMA-3 model.  
It outputs a match verdict (ACCEPTED/REJECTED) along with improvement suggestions — acting as an intelligent AI career coach.

---

## Features

- 📄 Uploads **job description** and **resume** as PDFs
- 🧠 Uses **Groq LLM (LLaMA 3)** for contextual matching
- 📝 Provides **structured feedback**:
  - Verdict: ACCEPTED or REJECTED
  - Skill and format improvement suggestions
- 🌐 (Planned) Google Calendar & Gmail integration for interview follow-ups

---

## Tech Stack

| Component        | Tech                          |
|------------------|-------------------------------|
| UI               | Streamlit                     |
| PDF Parsing      | PyPDF2                        |
| LLM              | Groq API (LLaMA 3 - 8B)        |
| Prompting        | LangChain PromptTemplate      |
| Google APIs      | OAuth (Gmail & Calendar scopes) |

---

## 🧪 How it Works

1. Upload **resume** and **job description**
2. Text is extracted from both
3. A structured **prompt** is built and sent to Groq
4. AI returns:
   - Verdict (ACCEPTED or REJECTED)
   - Suggestions for improvement

---

## 🏁 Getting Started

```bash
pip install -r requirements.txt
⚠️ Add your Groq API key to the script before running.

📂 File Overview
bash
aiResume-main/
├── main.py               # Streamlit app logic
├── client_secret.json    # (For Gmail/Calendar integration)
├── README.md             # You're reading it
Author
Hasini Uppaluri
