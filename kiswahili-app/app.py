"""
app.py
------

Main entry point for the Kiswahili Language Intelligence Engine UI.

This file connects Cepha's Streamlit interface to the real FastAPI
morphology backend.

Run with:

    streamlit run app.py
"""

import streamlit as st

from backend_client import analyze

from components.styling import inject_custom_css, render_theme_toggle
from components.input_panel import render_input_panel
from components.morphology_display import render_morphology
from components.explanation import render_explanation, render_ask_box


# ---------------------------------------------------------------------------
# PAGE CONFIGURATION
# ---------------------------------------------------------------------------

st.set_page_config(
    page_title="Kiswahili Language Intelligence Engine",
    page_icon="🇹🇿",
    layout="centered",
)


# ---------------------------------------------------------------------------
# EXISTING UI STYLING
# ---------------------------------------------------------------------------

_theme_mode = render_theme_toggle()
inject_custom_css(_theme_mode)


# ---------------------------------------------------------------------------
# SESSION STATE
# ---------------------------------------------------------------------------

if "last_result" not in st.session_state:
    st.session_state.last_result = None

if "last_input_type" not in st.session_state:
    st.session_state.last_input_type = None

if "last_input_text" not in st.session_state:
    st.session_state.last_input_text = None


# ---------------------------------------------------------------------------
# MAIN APPLICATION
# ---------------------------------------------------------------------------

def main():

    # -----------------------------------------------------------------------
    # HEADER
    # -----------------------------------------------------------------------

    st.title("Kiswahili Language Intelligence Engine")
    st.caption("From words to understanding")
    


    # -----------------------------------------------------------------------
    # INPUT
    # -----------------------------------------------------------------------

    with st.container(border=True):
        input_type, text, analyze_clicked = render_input_panel()


    # -----------------------------------------------------------------------
    # ANALYZE BUTTON
    # -----------------------------------------------------------------------

    if analyze_clicked:

        if not text.strip():

            st.warning(
                "Please enter a valid Kiswahili word or sentence."
            )

        elif input_type == "Question":

            st.info(
                "For questions about an analysis, first analyze a "
                "Kiswahili word or sentence."
            )

        else:

            with st.spinner(
                "Analyzing with the Kiswahili NLP engine..."
            ):

                try:

                    # Send input to the real FastAPI backend
                    result = analyze(
                        text,
                        input_type=input_type
                    )

                    # Save the real backend result
                    st.session_state.last_result = result
                    st.session_state.last_input_type = input_type
                    st.session_state.last_input_text = text

                except Exception as e:

                    st.error(
                        "We could not analyze this input right now."
                    )

                    st.caption(
                        f"Backend error: {e}"
                    )


    # -----------------------------------------------------------------------
    # DISPLAY LAST RESULT
    # -----------------------------------------------------------------------

    result = st.session_state.last_result


    if result:

        # -------------------------------------------------------------------
        # SHOW CURRENT INPUT
        # -------------------------------------------------------------------

        st.markdown(
            f"**Analyzing:** `{st.session_state.last_input_text}`"
        )


        # ===================================================================
        # WORD ANALYSIS
        # ===================================================================

        if isinstance(result, dict) and "grammar" not in result:

            # ---------------------------------------------------------------
            # Morphology
            # ---------------------------------------------------------------

            with st.container(border=True):

                render_morphology(result)


            # ---------------------------------------------------------------
            # Explanation + RAG
            # ---------------------------------------------------------------

            with st.container(border=True):

                render_explanation(result)


            # ---------------------------------------------------------------
            # Question & Answer
            # ---------------------------------------------------------------

            with st.container(border=True):

                render_ask_box(result)


        # ===================================================================
        # SENTENCE ANALYSIS
        # ===================================================================

        elif isinstance(result, dict) and "grammar" in result:

            # ---------------------------------------------------------------
            # Get sentence analysis and grammar result
            # ---------------------------------------------------------------

            sentence_analyses = result.get("analysis", [])
            grammar_result = result.get("grammar")


            st.subheader("Sentence Analysis")


            # ---------------------------------------------------------------
            # Check whether words were returned
            # ---------------------------------------------------------------

            if not sentence_analyses:

                st.warning(
                    "The NLP engine did not return any analyzable words."
                )


            else:

                # -----------------------------------------------------------
                # WORD-BY-WORD MORPHOLOGICAL ANALYSIS
                # -----------------------------------------------------------

                for index, word_analysis in enumerate(
                    sentence_analyses,
                    start=1
                ):

                    word = word_analysis.get(
                        "word",
                        f"Word {index}"
                    )

                    with st.container(border=True):

                        st.markdown(
                            f"### Word {index}: `{word}`"
                        )

                        render_morphology(word_analysis)

                        render_explanation(word_analysis)


                # -----------------------------------------------------------
                # SENTENCE-LEVEL GRAMMAR ANALYSIS
                # -----------------------------------------------------------

                with st.container(border=True):

                    st.subheader("Grammar Analysis")


                    if grammar_result:

                        is_correct = grammar_result.get(
                            "is_grammatically_correct"
                        )

                        score = grammar_result.get(
                            "grammar_score"
                        )

                        errors = grammar_result.get(
                            "errors",
                            []
                        )

                        warnings = grammar_result.get(
                            "warnings",
                            []
                        )


                        # ---------------------------------------------------
                        # Overall result
                        # ---------------------------------------------------

                        if is_correct:

                            st.success(
                                "The grammar engine found no grammatical errors."
                            )

                        else:

                            st.error(
                                "The grammar engine detected grammatical issues."
                            )


                        # ---------------------------------------------------
                        # Grammar score
                        # ---------------------------------------------------

                        if score is not None:

                            st.metric(
                                "Grammar Score",
                                f"{score}/100"
                            )


                        # ---------------------------------------------------
                        # Errors
                        # ---------------------------------------------------

                        if errors:

                            st.markdown("**Errors**")

                            for error in errors:

                                st.error(error)


                        # ---------------------------------------------------
                        # Grammar feedback
                        # ---------------------------------------------------

                        if warnings:

                            st.markdown("**Grammar Feedback**")

                            for warning in warnings:

                                st.info(warning)


                    else:

                        st.info(
                            "No grammar result was returned by the backend."
                        )


                # -----------------------------------------------------------
                # SENTENCE Q&A INFORMATION
                # -----------------------------------------------------------

                with st.container(border=True):

                    st.subheader("Ask the Language Engine")

                    st.info(
                        "For the current prototype, questions are answered "
                        "for individual word analyses. Analyze an individual "
                        "word separately to use the Q&A feature."
                    )


    # -----------------------------------------------------------------------
    # NO RESULT YET
    # -----------------------------------------------------------------------

    else:

        st.info(
            "Enter a Kiswahili word or sentence above and click "
            "Analyze to begin."
        )




# ---------------------------------------------------------------------------
# APPLICATION ENTRY POINT
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    main()
