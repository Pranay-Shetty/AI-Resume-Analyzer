import streamlit as st

# ----------------------------
# Components
# ----------------------------
from components.header import show_header
from components.sidebar import show_sidebar
from components.score_card import show_score
from components.skills_panel import show_skills
from components.footer import show_footer

# ----------------------------
# Resume Parsers
# ----------------------------
from parser.pdf_parser import extract_pdf_text
from parser.docx_parser import extract_docx_text

# ----------------------------
# Utilities
# ----------------------------
from utils.text_cleaner import clean_text
from utils.skills import extract_skills

# ----------------------------
# Services
# ----------------------------
from services.skill_matcher import compare_skills
from services.ats_scorer import calculate_ats_score


# =====================================
# Header & Sidebar
# =====================================

show_header()
show_sidebar()

# =====================================
# User Input
# =====================================

st.subheader("Upload Resume")

uploaded_resume = st.file_uploader(
    "Upload Resume",
    type=["pdf", "docx"]
)

job_description = st.text_area(
    "Paste Job Description",
    height=250,
    placeholder="Paste the job description here..."
)

# =====================================
# Analyze Resume
# =====================================

if st.button("Analyze Resume", use_container_width=True):

    # ----------------------------
    # Validation
    # ----------------------------

    if uploaded_resume is None:
        st.error("Please upload your resume.")
        st.stop()

    if not job_description.strip():
        st.error("Please paste a Job Description.")
        st.stop()

    # ----------------------------
    # Resume Parsing
    # ----------------------------

    extension = uploaded_resume.name.split(".")[-1].lower()

    if extension == "pdf":
        resume_text = extract_pdf_text(uploaded_resume)

    elif extension == "docx":
        resume_text = extract_docx_text(uploaded_resume)

    else:
        st.error("Unsupported file type.")
        st.stop()

    # ----------------------------
    # Clean Text
    # ----------------------------

    resume_text = clean_text(resume_text)

    # ----------------------------
    # Extract Skills
    # ----------------------------

    resume_skills = extract_skills(resume_text)
    jd_skills = extract_skills(job_description)

    # ----------------------------
    # Skill Matching
    # ----------------------------

    matched, missing = compare_skills(
        resume_skills,
        jd_skills
    )

    # ----------------------------
    # ATS Score
    # ----------------------------

    ats_score = calculate_ats_score(
        resume_text,
        matched,
        jd_skills
    )

    # =====================================
    # Results
    # =====================================

    st.divider()

    show_score(ats_score)

    st.divider()

    show_skills(
        matched,
        missing
    )

    st.divider()
    
    st.subheader("🤖 AI Analysis")

    st.info(
        """
        AI-powered analysis is coming soon.

        Upcoming features:

        • ATS Explanation

        • Resume Strengths

        • Resume Weaknesses

        • Missing Keywords

        • Resume Improvement Suggestions

        • Professional Summary Generation
        """
    )
    
    with st.expander("📄 Resume Preview"):

        st.text_area(
            "",
            resume_text,
            height=350
        )

show_footer()