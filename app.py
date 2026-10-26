
import streamlit as st
from dotenv import load_dotenv

from search import search_web
from processor import process_results
from generator import generate_report

load_dotenv()
@st.cache_data(ttl=600)
def cached_search(question):
    return search_web(question)

st.set_page_config(
    page_title="AI Research Assistant",
    page_icon="🔎",
    layout="wide"
)

st.title("🔎 AI Research Assistant")
st.write(
    "Ask a question and get an AI-generated research report "
    "based on web search results."
)

question = st.text_input(
    "Enter your research question",
    placeholder="e.g. How is AI being used in healthcare?"
)

if st.button("Research"):
    if not question.strip():
        st.warning("Please enter a research question.")

    else:
        try:
            with st.spinner("Searching the web..."):
               results = cached_search(question)
            cleaned_results = process_results(results)

            if not cleaned_results:
                st.warning(
                    "No useful search results found. "
                    "Try another question."
                )
            else:
                with st.spinner("Generating your research report..."):
                    report = generate_report(
                        question,
                        cleaned_results
                    )

                st.subheader("Research Report")
                st.markdown(report)

                st.subheader("Web Sources")
                for item in cleaned_results:
                    st.markdown(
                        f"- [{item['title']}]({item['url']})"
                    )

        except ValueError as e:
            st.error(f"Configuration problem: {e}")

        except Exception:
            st.error(
                "Something went wrong while researching. "
                "Please try again. If the problem continues, "
                "check the terminal for the technical error."
            )
