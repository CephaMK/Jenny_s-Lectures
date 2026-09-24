"""
explanation.py
----------------
Renders the plain-language explanation of the analysis. This is what turns
the project from a technical NLP demo into a language-learning product.
"""

import streamlit as st


def render_explanation(result: dict):
    st.subheader("Explanation")
    explanation = result.get("explanation")
    if explanation:
        st.write(explanation)
    else:
        st.write("No explanation available for this input yet.")


def render_ask_box():
    """
    'Ask the language engine' box. In Phase 1 this just echoes a canned
    answer — later this is where the RAG/chatbot (Phase 7) plugs in.
    """
    st.subheader("Ask the Language Engine")
    question = st.text_input(
        "Ask a question about the analysis",
        placeholder='e.g. Why is "ni" used in this word?',
        key="ask_question_text",
    )
    if st.button("Ask", key="ask_button"):
        if question.strip():
            st.info(
                "This is a placeholder answer. Once the RAG/chatbot "
                "(Phase 7) is connected, this will pull a real explanation "
                "from the Kiswahili corpus."
            )
        else:
            st.warning("Please type a question first.")
