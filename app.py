import streamlit as st
import id_spacy
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression

# Load the pre-trained NER model
nlp = id_spacy.load()

# Function to predict sentiment
def predict_sentiment(text):
    # Process the text data with the NER model and extract named entities
    doc = nlp(text)
    named_entities = [ent.text for ent in doc.ents]
    named_entities_data = ' '.join(named_entities)
    
    # Transform named entities into features
    X = vectorizer.transform([named_entities_data])
    
    # Predict sentiment label
    prediction = lr.predict(X)
    return prediction[0]

# Main function for Streamlit app
def main():
    st.title("Analisis Sentimen dengan NER (Named Entity Recognition)")
    
    # Text input for user to input new text data
    user_input = st.text_area("Masukkan teks untuk analisis sentimen:")
    
    if st.button("Prediksi Sentimen"):
        if user_input.strip() == "":
            st.error("Mohon masukkan teks untuk dilakukan analisis sentimen.")
        else:
            # Predict sentiment
            sentiment = predict_sentiment(user_input)
            st.success("Sentimen: {}".format(sentiment))

if __name__ == "__main__":
    # Load the trained logistic regression model and count vectorizer
    vectorizer = CountVectorizer()
    vectorizer.fit(named_entities_data)
    
    lr = LogisticRegression()
    lr.fit(X, sentiment_labels)
    
    # Run the Streamlit app
    main()
