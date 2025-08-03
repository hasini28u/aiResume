# 🧠 AI Resume Assistant — Resume Analysis & Generation (using LLMs)

This repository contains my implementation of an AI-powered resume assistant, developed using Natural Language Processing and Large Language Models, as part of my AI/ML training.

---

## 🚀 Project Overview

The AI Resume Assistant helps users:
- Analyze resumes for keywords, ATS compatibility, and role alignment
- Provide personalized feedback and suggestions for improvement
- Optionally generate formatted resume drafts using LLMs
- Export final resumes in PDF or Word formats
---

## 🛠 Tech Stack & Tools

- **Python** for core logic  
- **Jupyter Notebooks** for walkthroughs  
- NLP model pipeline: spaCy, NLTK, or Hugging Face Transformers  
- LLM integration using OpenAI or Google Gemini APIs  
- File parsing tools: PyPDF2, python-docx, or equivalent  
- Streamlit (optional) for a demo UI

---

## 🧪 Key Features

- 🛠 **Resume Parsing & Analysis**  
  Extract sections like experience, education, skills, and match them to job descriptions.

- 🔍 **Keyword Gap & ATS Score**  
  Identify missing keywords and assess ATS readiness.

- ✍️ **AI-Driven Suggestions & Generation**  
  Curate resume content tailored to specific roles or improve existing bullet points.

- 📤 **Resume Export**  
  Output improved resumes in PDF or DOCX formats.

---

## ⚡ How to Use / Run the Code

1. **Clone the repo**  
   ```bash
   git clone https://github.com/hasini28u/aiResume.git
   cd aiResume
Install dependencies

bash
Copy
Edit
pip install -r requirements.txt
Set up environment variables

bash
Copy
Edit
export OPENAI_API_KEY="your_key_here"
# or
export GOOGLE_API_KEY="your_gemini_key_here"
Run analysis or generation

bash
Copy
Edit
python src/analyze_resume.py --input your_resume.pdf
python src/generate_resume.py --role "data analyst"
Open notebooks for examples and experimentation:

bash
Copy
Edit
jupyter notebook notebooks/resume_analysis.ipynb
(Optional) Launch demo (if Streamlit included):

bash
Copy
Edit
streamlit run app.py
🎓 Learning Outcomes
During this project, I gained practical experience in:

Resume parsing using NLP techniques

Evaluating ATS compatibility and keyword matching

Fine-tuning LLM prompts for content generation

Building end-to-end pipelines for input → analysis → output

📬 Connect with Me
💼 LinkedIn: www.linkedin.com/in/hasini-uppaluri-387a592a2

📧 Email: hasiniuppaluri@gmail.com
