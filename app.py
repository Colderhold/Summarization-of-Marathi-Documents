import streamlit as st
from text_rank_positional_Marathi import process as positional_process
from text_rank_similarity_Marathi import textRankSimilarity

def main():
    st.markdown("<h1 style='text-align: center;'>Text Summarization of Marathi Documents</h1>", unsafe_allow_html=True)

    # Dropdown for method selection
    summarization_method = st.selectbox(
        "Select Summarization Method",
        ("Positional", "Similarity")
    )

    # File uploader
    uploaded_file = st.file_uploader("Upload a Marathi text file", type=['txt'], accept_multiple_files=False)

    if uploaded_file is not None:
        # Read uploaded file
        text_data = uploaded_file.read().decode('utf-8')

        st.subheader("Input Text")
        st.markdown(f"<div style='text-align: justify;'>{text_data}</div>", unsafe_allow_html=True)

        # Process based on the selected method
        if summarization_method == "Positional":
            result = positional_process(text_data)
        elif summarization_method == "Similarity":
            result = textRankSimilarity(text_data)
        else:
            result = None

        # Display summarized text
        if result:
            st.subheader("Summarized Text")
            st.markdown(f"<div style='text-align: justify;'>{result}</div>", unsafe_allow_html=True)
        else:
            st.error("Failed to generate a summary. Please check the input file.")

if __name__ == "__main__":
    main()
