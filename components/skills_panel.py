import streamlit as st


def create_chip(skill, color):

    return f"""
    <span style="
        display:inline-block;
        padding:8px 14px;
        margin:6px;
        border-radius:20px;
        background-color:{color};
        color:white;
        font-weight:600;
        font-size:14px;
    ">
        {skill}
    </span>
    """


def show_skills(matched, missing):

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("✅ Matched Skills")

        if matched:

            html = ""

            for skill in sorted(matched):
                html += create_chip(skill, "#28a745")

            st.markdown(html, unsafe_allow_html=True)

        else:
            st.info("No matched skills found.")

    with col2:

        st.subheader("❌ Missing Skills")

        if missing:

            html = ""

            for skill in sorted(missing):
                html += create_chip(skill, "#dc3545")

            st.markdown(html, unsafe_allow_html=True)

        else:
            st.success("No missing skills 🎉")