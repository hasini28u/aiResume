import streamlit as st
from google_auth_oauthlib.flow import InstalledAppFlow
from PyPDF2 import PdfReader
from langchain.prompts import PromptTemplate
from groq import Groq

# API Key for Groq (add your actual key here)
api_key = "api_key"
SCOPES = ['https://www.googleapis.com/auth/calendar', 'https://www.googleapis.com/auth/gmail.send']

# Function to extract text from a PDF
def extract_text_from_pdf(pdf_file):
    reader = PdfReader(pdf_file)
    text = "".join(page.extract_text() for page in reader.pages)
    return text

# Function to assess resume suitability with feedback
def assess_suitability_with_feedback(job_description, resume):
    prompt_template = PromptTemplate(
        input_variables=["resume", "job_description"],
        template=(
            "You are a career coach. Analyze the resume against the job description below.\n\n"
            "Job Description:\n{job_description}\n\n"
            "Candidate Resume:\n{resume}\n\n"
            "Provide the following:\n"
            "1. A verdict (ACCEPTED or REJECTED) on whether the resume matches the job.\n"
            "2. Suggestions to improve the resume, focusing on missing skills, formatting, and alignment with the job description."
        ),
    )

    query = prompt_template.format(job_description=job_description, resume=resume)
    client = Groq(api_key=api_key)

    response = client.chat.completions.create(
        messages=[{"role": "system", "content": "You are an expert career coach."},
                  {"role": "user", "content": query}],
        model="llama3-8b-8192",
    )

    return response.choices[0].message.content

# Streamlit interface
def resume_check():
    st.title("Resume Screening and Interview Management System")

    # Upload job description PDF
    job_desc_file = st.file_uploader("Upload Job Description PDF", type=["pdf"])
    if job_desc_file is not None:
        job_description = extract_text_from_pdf(job_desc_file)

        # Upload resume PDF
        resume_file = st.file_uploader("Upload Resume PDF", type=["pdf"])
        if resume_file is not None:
            resume = extract_text_from_pdf(resume_file)

            # Assess suitability with feedback
            feedback = assess_suitability_with_feedback(job_description, resume)

            # Display the feedback
            st.subheader("Resume Screening Result")
            st.write(feedback)
        else:
            st.warning("Please upload a resume PDF.")
    else:
        st.warning("Please upload a job description PDF.")

# Run the Streamlit app
if __name__ == "__main__":
    resume_check()
