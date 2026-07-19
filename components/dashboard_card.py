import streamlit as st


def dashboard_card(title, value, subtitle="", icon=""):

    st.markdown(
        f"""
<div style="
background:#1E293B;
border:1px solid #334155;
border-radius:20px;
padding:20px;
box-shadow:0 12px 28px rgba(0,0,0,.35);
">

# {icon}

### {title}

# {value}

{subtitle}

</div>
""",
        unsafe_allow_html=True,
    )