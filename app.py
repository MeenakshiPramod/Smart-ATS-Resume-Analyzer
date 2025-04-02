import streamlit as st
import google.generativeai as genai
import os
import PyPDF2 as pdf
import re  # Import the regular expression library
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv('API_KEY'))

def get_gemini_response(input_prompt):
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(input_prompt)
    return response.text


def input_pdf_text(uploaded_file):
    reader = pdf.PdfReader(uploaded_file)
    text = ""
    for page in range(len(reader.pages)):
        page = reader.pages[page]
        text += str(page.extract_text())
    return text


# Prompt Template -  Improved Robustness
input_prompt_template = """
Hey Act Like a skilled and experienced ATS (Application Tracking System)
with a deep understanding of the tech field, including software engineering,
data science, data analysis, and big data engineering. Your task is to evaluate
the resume based on the given job description.  Consider that the job market
is very competitive, and provide the best possible assistance for improving
the resume.

Specifically:

1.  **Calculate a Job Description Match Percentage:**  Assess how well the resume
    aligns with the job description, assigning a percentage match. Provide only the number with the percent sign. For example: 85%

2.  **Identify Missing Keywords:**  List any crucial keywords from the job
    description that are missing from the resume. Focus on technical skills,
    tools, and technologies. Separate each keyword by comma. For example: Python, Java, C++

3.  **Generate a Profile Summary:**  Write a concise (around 50-75 words)
    professional summary that highlights the candidate's strengths and
    experience, tailored to the job description.  The summary should
    emphasize skills and experiences relevant to the role.

Output the response in the following format.  It is VERY IMPORTANT that you use these exact headings, and only include the content described.  Do not add any extra text.

Job Description Match: [Percentage]%
Missing Keywords: [Comma-separated list of missing keywords]
Profile Summary: [A concise and compelling professional summary tailored to the job description]

resume: {resume_text}
description: {jd}

"""


## streamlit app
st.title("Smart ATS Resume Analyzer")
st.markdown("Upload your resume and the job description to see how well they match!")
jd = st.text_area("Paste the Job Description", height=200)
uploaded_file = st.file_uploader(
    "Upload Your Resume (PDF)", type="pdf", help="Please upload a PDF file"
)

submit = st.button("Analyze")


def display_results(results):
    """Displays the analysis results in a human-readable format using regular expressions."""
    try:
        # Use regular expressions to extract the information more robustly
        match_match = re.search(r"Job Description Match:\s*([0-9]+%)", results)
        match_keywords = re.search(r"Missing Keywords:\s*(.+)", results, re.DOTALL)
        match_summary = re.search(r"Profile Summary:\s*(.+)", results, re.DOTALL)  #re.DOTALL to match across newlines

        if match_match:
            match_percentage = match_match.group(1).strip()
            st.subheader("Job Description Match")
            st.write(f"> {match_percentage}")
        else:
            st.error("Could not extract Job Description Match.")

        if match_keywords:
            missing_keywords = match_keywords.group(1).strip()
            st.subheader("Missing Keywords")
            st.write(f"> {missing_keywords}")
        else:
            st.error("Could not extract Missing Keywords.")

        if match_summary:
            profile_summary = match_summary.group(1).strip()
            st.subheader("Profile Summary")
            st.write(f"> {profile_summary}")
        else:
            st.error("Could not extract Profile Summary.")

    except Exception as e:
        st.error(f"Error processing results: {e}. Raw Response: {results}")


if submit:
    if uploaded_file is not None and jd:
        try:
            text = input_pdf_text(uploaded_file)
            # Use the template and pass the extracted text and JD
            input_prompt = input_prompt_template.format(resume_text=text, jd=jd)
            response = get_gemini_response(input_prompt)
            display_results(response)

        except Exception as e:
            st.error(f"An error occurred: {e}")
    elif not jd:
        st.warning("Please paste the job description.")
    else:
        st.warning("Please upload your resume.")