import streamlit as st


def show_score(score):

    st.subheader("📊 ATS Compatibility Score")

    st.metric(
        label="Overall Score",
        value=f"{score}/100"
    )

    st.progress(score / 100)