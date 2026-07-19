import streamlit as st


def show_sidebar():

    with st.sidebar:

        st.header("📋 Menu")

        st.info(
            """
            ### AI Resume Analyzer

            Version **1.0**

            #### Features

            ✅ Resume Parsing

            ✅ ATS Score

            ✅ Skill Matching

            🔜 AI Suggestions

            🔜 Cover Letter Generator

            🔜 Interview Questions
            """
        )

        st.markdown("---")

        st.write("Developed using")

        st.write("🐍 Python")

        st.write("⚡ Streamlit")

        st.write("🤖 OpenAI")