"""
app.py
-------
Main entry point for the Kiswahili Language Intelligence Engine UI.

Run with:
    streamlit run app.py

This file is intentionally thin: it just wires together the components
and the backend_client. All display logic lives in components/, and all
data-fetching logic lives in backend_client.py.
"""

import streamlit as st

from backend_client import analyze
from components.styling import inject_custom_css, render_theme_toggle
from components.input_panel import render_input_panel
from components.morphology_display import render_morphology
from components.grammar_display import render_grammar
from components.explanation import render_explanation, render_ask_box

st.set_page_config(
    page_title="Kiswahili Language Intelligence Engine",
    page_icon="🇹🇿",
    layout="centered",
)

_theme_mode = render_theme_toggle()
inject_custom_css(_theme_mode)

# Keep the last result in session_state so it persists across reruns
# (e.g. when the user interacts with the "Ask" box below).
if "last_result" not in st.session_state:
    st.session_state.last_result = None


def main():
    st.title("Kiswahili Language Intelligence Engine")
    st.caption("From words to understanding")

    with st.container(border=True):
        input_type, text, analyze_clicked = render_input_panel()

    if analyze_clicked:
        if not text.strip():
            st.warning("⚠️ Please enter a valid Kiswahili word or sentence.")
        else:
            with st.spinner("Analyzing..."):
                try:
                    result = analyze(text)
                    st.session_state.last_result = result
                except Exception:
                    st.error(
                        "⚠️ We could not analyze this input right now. "
                        "Please try again in a moment."
                    )

    result = st.session_state.last_result
    if result:
        with st.container(border=True):
            render_morphology(result)
        with st.container(border=True):
            render_grammar(result)
        with st.container(border=True):
            render_explanation(result)
        with st.container(border=True):
            render_ask_box()
    else:
        st.info("Enter a Kiswahili word or sentence above and click Analyze to begin.")


if __name__ == "__main__":
    main()
