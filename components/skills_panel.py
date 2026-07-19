import streamlit as st


def show_skills(matched, missing):

    left, right = st.columns(2)

    with left:

        st.success("✅ Matched Skills")

        if matched:
            for skill in matched:
                st.write(f"• {skill}")
        else:
            st.write("No matching skills found.")

    with right:

        st.error("❌ Missing Skills")

        if missing:
            for skill in missing:
                st.write(f"• {skill}")
        else:
            st.write("No missing skills detected.")