import streamlit as st


def show_hero():
    st.markdown(
        """
        <div class="hero">
            <h1>🤖 AI Resume Analyzer</h1>
            <div class="hero-text">
                Analyze your resume against any job description using AI.<br><br>
                Get ATS scoring, skill matching, recruiter insights,
                missing keywords and personalized recommendations.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )