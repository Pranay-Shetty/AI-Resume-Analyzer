from parser.pdf_parser import extract_pdf_text
from parser.docx_parser import extract_docx_text
from utils.text_cleaner import clean_text
from utils.skills import extract_skills
from services.skill_matcher import compare_skills
import streamlit as st

st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="wide"
)

st.title("📄 AI Resume Analyzer")

st.markdown("""
Welcome! Upload your resume and compare it against a Job Description using AI.

This application will:
- 📄 Read your resume
- 🎯 Compare it with a Job Description
- 📊 Calculate an ATS score
- 💡 Suggest improvements
""")

uploaded_resume = st.file_uploader(
    "Upload Resume",
    type=["pdf", "docx"]
)

job_description = st.text_area(
    "Paste Job Description",
    height=250,
    placeholder="Paste the job description here..."
)

if st.button("Analyze Resume"):

    if uploaded_resume is None:
        st.error("Please upload your resume.")

    elif not job_description.strip():
        st.error("Please paste a Job Description.")

    else:

        file_extension = uploaded_resume.name.split(".")[-1].lower()

        if file_extension == "pdf":
            resume_text = extract_pdf_text(uploaded_resume)
            resume_text = clean_text(resume_text)
            resume_skills = extract_skills(resume_text)
            jd_skills = extract_skills(job_description)
            matched, missing = compare_skills(resume_skills,jd_skills)

        elif file_extension == "docx":
            resume_text = extract_docx_text(uploaded_resume)
            resume_text = clean_text(resume_text)
            resume_skills = extract_skills(resume_text)
            jd_skills = extract_skills(job_description)
            matched, missing = compare_skills(resume_skills,jd_skills)

        else:
            st.error("Unsupported file type.")
            st.stop()

        st.success("Resume Parsed Successfully!")

        st.subheader("Extracted Resume Text")

        st.text_area(
            "",
            resume_text,
            height=400
        )
        #Display Results
        st.subheader("Detected Resume Skills")
        st.write(resume_skills)

        st.subheader("Detected Job Skills")
        st.write(jd_skills)

        col1, col2 = st.columns(2)

        with col1:
            st.success("Matched Skills")
            for skill in matched:
                st.write(f"✅ {skill}")

        with col2:
            st.error("Missing Skills")
            for skill in missing:
                st.write(f"❌ {skill}")