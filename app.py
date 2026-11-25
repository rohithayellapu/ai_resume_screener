import streamlit as st

from resume_parser import extract_text
from similarity import calculate_similarity
from recommendation import get_missing_skills

st.set_page_config(page_title="AI Resume Screener", page_icon="📄")

st.title(" Personalized AI Resume Screener")

st.write("Upload your Resume and Job Description")

resume_file = st.file_uploader(
    "Upload Resume",
    type=["pdf", "docx"]
)

jd_text = st.text_area(
    "Paste Job Description Here",
    height=250
)

if resume_file and jd_text:

    resume_text = extract_text(resume_file)

    score = calculate_similarity(resume_text, jd_text)

    st.subheader(f"Resume Match Score: {score}%")

    missing_skills = get_missing_skills(resume_text, jd_text)

    st.subheader("Missing Skills")

    if missing_skills:
        for skill in missing_skills:
            st.write(f"• {skill}")
    else:
        st.success(" No missing skills found.")