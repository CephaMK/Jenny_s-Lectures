"""
input_panel.py
---------------
Renders the input section: lets the user choose Word / Sentence / Question
and type their Kiswahili input. Returns (input_type, text, analyze_clicked).
"""

import streamlit as st


def render_input_panel():
    st.subheader("Input")

    input_type = st.radio(
        "Input type",
        options=["Word", "Sentence", "Question"],
        horizontal=True,
        label_visibility="collapsed",
    )

    placeholder_map = {
        "Word": "e.g. kitabu",
        "Sentence": "e.g. Ninampenda mtoto.",
        "Question": "e.g. What is the tense of this verb?",
    }

    text = st.text_input(
        f"Enter Kiswahili ({input_type.lower()})",
        placeholder=placeholder_map[input_type],
        key="user_input_text",
    )

    analyze_clicked = st.button("Analyze", type="primary", use_container_width=True)

    return input_type, text, analyze_clicked
