import streamlit as st


def show_header():

    st.set_page_config(
        page_title="AI Resume Analyzer",
        page_icon="📄",
        layout="wide"
    )

    st.title("📄 AI Resume Analyzer")

    st.caption(
        "Analyze your resume against any job description using AI"
    )

    st.markdown("---")