# Summarization of Marathi Documents

This project implements a text summarization system specifically for documents written in Marathi. It uses an extractive approach to condense large volumes of text into a concise summary, retaining essential meaning and key points. The summarization process is based on natural language processing (NLP) techniques tailored for the Marathi language.

## Project Overview

This summarization system works by identifying and ranking the most important sentences within a Marathi document. Using preprocessing, stemming, and sentence ranking techniques, the system builds a summary that provides readers with a quick understanding of the main content.

## How It Works

The project operates in three main stages to process and summarize Marathi text:

1. **Preprocessing**: 
   - **Tokenization**: Breaks down the input text into individual tokens (words or phrases).
   - **Stopword Removal**: Removes common Marathi stopwords (such as prepositions and conjunctions) that don’t add significant meaning, using a custom Marathi stopword list.
   
2. **Stemming**: 
   - A rule-based Marathi stemmer is used to reduce words to their base or root forms, helping in normalizing similar words to a common base.

3. **Sentence Ranking**:
   - **TextRank Algorithm**: A graph-based ranking model inspired by PageRank is applied to identify the most relevant sentences. The algorithm ranks sentences based on keyword extraction and other linguistic features.
   - **Graph Construction**: A graph is created where sentences act as vertices, and edges represent connections based on sentence similarity or keyword presence.
   - **Sentence Extraction**: The top-ranked sentences are extracted to form the final summary.

4. **Summary Output**: 
   - The system displays the summarized text, offering a shortened version that conveys the main points of the input document.

## Key Features
- **Language-Specific Processing**: Tailored tokenization, stopword removal, and stemming specifically for Marathi.
- **Graph-Based Ranking**: Uses TextRank to assign scores to sentences and determine their relevance for inclusion in the summary.

## Example Workflow
1. The user uploads a Marathi document.
2. The system preprocesses the text by tokenizing it and removing unnecessary stopwords.
3. Stemming is applied to normalize words.
4. TextRank ranks sentences, and the top sentences are chosen to create the summary.
5. The summarized text is displayed to the user.

This extractive summarization approach provides a clear, concise summary, making it easier to grasp the document's key points quickly.

## How to Use

### Prerequisites
- **Python 3.x**
- Required libraries: `streamlit`, `nltk`, and `networkx`

Install the dependencies:
```bash
pip install streamlit nltk networkx
```

Run command:
```bash
streamlit run app.py
```
