import plotly.graph_objects as go
import streamlit as st


def show_skill_chart(matched, missing):

    skills = list(matched) + list(missing)

    status = (
        ["Matched"] * len(matched)
        + ["Missing"] * len(missing)
    )

    colors = [
        "green" if s == "Matched" else "crimson"
        for s in status
    ]

    fig = go.Figure()

    fig.add_trace(
        go.Bar(
            x=skills,
            y=[1] * len(skills),
            marker_color=colors,
            text=status,
            textposition="inside",
        )
    )

    fig.update_layout(
        title="Skills Coverage",
        xaxis_title="Skills",
        yaxis=dict(
            visible=False
        ),
        height=450,
        showlegend=False,
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )