import streamlit as st
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from textblob import TextBlob
import nltk

# Download necessary NLTK data files
nltk.download('punkt')

# Initialize the PorterStemmer
stemmer = PorterStemmer()

# Title of the application
st.title("Aplikasi NLP Sederhana")

# Sidebar options
st.sidebar.header("Pilih Fungsi NLP")
options = st.sidebar.radio("Fungsi:", ("Tokenisasi", "Stemming", "Analisis Sentimen"))

# Input text from user
text_input = st.text_area("Masukkan teks di sini:", "")

if text_input:
    if options == "Tokenisasi":
        # Tokenization
        tokens = word_tokenize(text_input)
        st.write("Hasil Tokenisasi:")
        st.write(tokens)

    elif options == "Stemming":
        # Stemming
        tokens = word_tokenize(text_input)
        stemmed_tokens = [stemmer.stem(token) for token in tokens]
        st.write("Hasil Stemming:")
        st.write(stemmed_tokens)

    elif options == "Analisis Sentimen":
        # Sentiment Analysis
        blob = TextBlob(text_input)
        sentiment = blob.sentiment
        st.write("Hasil Analisis Sentimen:")
        st.write(f"Polarity: {sentiment.polarity}")
        st.write(f"Subjectivity: {sentiment.subjectivity}")

# Footer
st.sidebar.markdown("Dibuat dengan ❤️ menggunakan Streamlit")
