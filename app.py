import streamlit as st
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import string

# Download NLTK data
nltk.download('punkt')
nltk.download('stopwords')

# Function to preprocess text
def preprocess_text(text):
    # Convert to lowercase
    text = text.lower()
    
    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))
    
    # Tokenize text
    tokens = word_tokenize(text)
    
    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    tokens = [word for word in tokens if word not in stop_words]
    
    return ' '.join(tokens)

# Streamlit app
st.title("Text Preprocessing App")

st.write("Enter the text you want to preprocess:")

user_input = st.text_area("Input Text")

if st.button("Preprocess"):
    if user_input:
        processed_text = preprocess_text(user_input)
        st.write("Processed Text:")
        st.write(processed_text)
    else:
        st.write("Please enter some text to preprocess.")
