import streamlit as st

# ==========================
# Components
# ==========================
from components.header import show_header
from components.sidebar import show_sidebar
from components.score_card import show_score
from components.skills_panel import show_skills
from components.footer import show_footer

# ==========================
# Resume Parsers
# ==========================
from parser.pdf_parser import extract_pdf_text
from parser.docx_parser import extract_docx_text

# ==========================
# Utilities
# ==========================
from utils.text_cleaner import clean_text
from utils.skills import extract_skills

# ==========================
# Services
# ==========================
from services.skill_matcher import compare_skills
from services.ats_scorer import calculate_ats_score
from services.openai_service import analyze_resume


# =====================================
# Page
# =====================================

show_header()
show_sidebar()

# =====================================
# Upload Section
# =====================================

st.subheader("📄 Upload Resume")

uploaded_resume = st.file_uploader(
    "Choose your resume",
    type=["pdf", "docx"]
)

job_description = st.text_area(
    "Paste Job Description",
    height=250,
    placeholder="Paste the job description here..."
)

# =====================================
# Analyze Button
# =====================================

if st.button("🚀 Analyze Resume", use_container_width=True):

    # ----------------------------
    # Validation
    # ----------------------------

    if uploaded_resume is None:
        st.error("Please upload a resume.")
        st.stop()

    if not job_description.strip():
        st.error("Please paste a job description.")
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
        st.error("Unsupported file format.")
        st.stop()

    # ----------------------------
    # Clean Resume
    # ----------------------------

    resume_text = clean_text(resume_text)

    # ----------------------------
    # Extract Skills
    # ----------------------------

    resume_skills = extract_skills(resume_text)
    jd_skills = extract_skills(job_description)

    # ----------------------------
    # Match Skills
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

    # =====================================
    # AI Analysis
    # =====================================

    st.divider()

    st.header("🤖 AI Resume Analysis")

    with st.spinner("Analyzing resume using AI..."):

        analysis = analyze_resume(resume_text, job_description)

    if analysis is None:
        st.error(
            "❌ AI returned an invalid response. Please try again."
        )

    else:

        score_col, summary_col = st.columns([1, 2])

        with score_col:
            st.metric(
                "AI ATS Score",
                f"{analysis.ats_score}/100"
            )

        with summary_col:
            st.info(
                analysis.professional_summary
            )

        st.divider()

        left, right = st.columns(2)

        with left:

            st.success("💪 Strengths")

            for strength in analysis.strengths:
                st.write(f"✅ {strength}")

        with right:

            st.error("⚠ Weaknesses")

            for weakness in analysis.weaknesses:
                st.write(f"❌ {weakness}")

        st.divider()

        st.warning("📌 Missing Skills")

        for skill in analysis.missing_skills:
            st.write(f"• {skill}")

        st.divider()

        st.subheader("🚀 Suggestions")

        for suggestion in analysis.suggestions:
            st.write(f"✔ {suggestion}")

    # =====================================
    # Resume Preview
    # =====================================

    st.divider()

    with st.expander("📄 Resume Preview"):

        st.text_area(
            "",
            resume_text,
            height=350
        )

# =====================================
# Footer
# =====================================

show_footer()