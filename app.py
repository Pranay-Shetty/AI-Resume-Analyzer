import streamlit as st

# ==========================
# Components
# ==========================
from components.header import show_header
from components.sidebar import show_sidebar
from components.score_card import show_score
from components.skills_panel import show_skills
from components.footer import show_footer
from components.charts import show_skill_chart
from components.hero import show_hero
from components.upload_panel import render_upload_panel

# =========================
# Pages
# =========================
from pages.analysis_tab import render_analysis_tab
from pages.ai_tab import render_ai_tab
from pages.resume_preview_tab import render_resume_tab

# =====================================
# Services
# =====================================
from services.resume_analyzer import analyze_resume_file

# =====================================
# CSS
# =====================================
st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded",
)

def load_css():
    with open("assets/styles.css") as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )
        
# =====================================
# Session State
# =====================================

if "analysis_complete" not in st.session_state:
    st.session_state.analysis_complete = False
    
# =====================================
# Page
# =====================================
load_css()
show_hero()
show_sidebar()

# =====================================
# Upload Section
# =====================================
uploaded_resume, job_description, analyze_clicked = render_upload_panel()

# =====================================
# Analyze Button
# =====================================

if analyze_clicked:

    if uploaded_resume is None:
        st.error("Please upload a resume.")
        st.stop()

    if not job_description.strip():
        st.error("Please paste a job description.")
        st.stop()

    try:
        analyze_resume_file(
            uploaded_resume,
            job_description
        )

        st.rerun()

    except Exception as e:
        st.error(str(e))

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
    
    total_skills = len(jd_skills)

    if total_skills > 0:
        skill_match_percentage = round(
            (len(matched) / total_skills) * 100
        )
    else:
        skill_match_percentage = 0

    # ----------------------------
    # ATS Score
    # ----------------------------

    ats_score = calculate_ats_score(
        resume_text,
        matched,
        jd_skills
    )
    # ----------------------------
    # AI Analysis
    # ----------------------------

    analysis = analyze_resume(
        resume_text,
        job_description
    )

    # ----------------------------
    # Save Everything
    # ----------------------------

    st.session_state.resume_text = resume_text
    st.session_state.matched = matched
    st.session_state.missing = missing
    st.session_state.ats_score = ats_score
    st.session_state.skill_match_percentage = skill_match_percentage
    st.session_state.analysis = analysis

    st.session_state.analysis_complete = True

    st.rerun()

# =====================================
# Results Tabs
# =====================================

if st.session_state.analysis_complete:
    tab1, tab2, tab3 = st.tabs([
        "📊 Analysis",
        "🤖 AI Insights",
        "📄 Resume Preview"
    ])
    
    with tab1:
        render_analysis_tab(
            st.session_state.ats_score,
            st.session_state.skill_match_percentage,
            st.session_state.matched,
            st.session_state.missing
        )

    with tab2:
        render_ai_tab(st.session_state.analysis)

    with tab3:
        render_resume_tab(st.session_state.resume_text)

# =====================================
# Footer
# =====================================

show_footer()