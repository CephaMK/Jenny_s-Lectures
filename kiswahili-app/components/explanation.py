import streamlit as st

from rag.retriever import retrieve_for_analysis
from rag.explainer import generate_explanation
from rag.qa import answer_question

def render_explanation(result: dict):

    st.subheader("Explanation")

    # Retrieve relevant knowledge
    retrieved = retrieve_for_analysis(result, top_k=3)

    # Generate explanation from the actual NLP analysis
    explanation = generate_explanation(
        result,
        retrieved_knowledge=retrieved
    )

    st.write(explanation)

    st.subheader("Retrieved Knowledge")

    if not retrieved:
        st.info(
            "No matching examples were found in the current "
            "Kiswahili knowledge base."
        )
        return

    for item in retrieved:

        sentence = item.get("sentence", "")
        analysis = item.get("analysis", "")
        number = item.get("number")

        with st.container(border=True):

            if number:
                st.caption(
                    f"Knowledge-base example #{number}"
                )

            st.markdown(f"**{sentence}**")

            if analysis:
                st.write(analysis)


def render_ask_box(result: dict):

    st.subheader("Ask the Language Engine")

    question = st.text_input(
        "Ask a question about the analysis",
        placeholder='e.g. Why is "a-" used in "anasoma"?',
        key="ask_question_text",
    )

    if st.button("Ask", key="ask_button"):

        if not question.strip():

            st.warning("Please type a question first.")
            return

        # Retrieve relevant knowledge
        retrieved = retrieve_for_analysis(
            result,
            top_k=3
        )

        # Generate answer using the actual analysis
        answer = answer_question(
            question,
            result,
            retrieved
        )

        st.markdown("### Answer")

        st.write(answer)