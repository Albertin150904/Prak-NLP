import streamlit as st
from google.oauth2 import service_account
from google.cloud import dialogflow_v2 as dialogflow

# Fungsi untuk menginisialisasi Dialogflow
@st.cache_resource
def initialize_dialogflow():
    st.write("Initializing Dialogflow...")
    credentials = service_account.Credentials.from_service_account_file("path/to/your/service-account-file.json")
    session_client = dialogflow.SessionsClient(credentials=credentials)
    session = session_client.session_path("your-project-id", "unique-session-id")
    return session_client, session

# Fungsi untuk mengirim teks ke Dialogflow dan mendapatkan respons
def detect_intent_texts(session_client, session, text, language_code='en'):
    st.write(f"Sending text to Dialogflow: {text}")
    text_input = dialogflow.types.TextInput(text=text, language_code=language_code)
    query_input = dialogflow.types.QueryInput(text=text_input)
    response = session_client.detect_intent(session=session, query_input=query_input)
    return response.query_result

# Inisialisasi sesi Dialogflow
try:
    session_client, session = initialize_dialogflow()
    st.write("Dialogflow initialized successfully.")
except Exception as e:
    st.write(f"Error initializing Dialogflow: {e}")

# Inisialisasi Streamlit
st.title("Dialogflow Chatbot with Streamlit")
st.write("Type a message and press Enter to chat with the bot:")

# Input pengguna
user_input = st.text_input("You:", "")

if user_input:
    try:
        # Mendapatkan respons dari Dialogflow
        response = detect_intent_texts(session_client, session, user_input)
        st.write("Bot: ", response.fulfillment_text)
    except Exception as e:
        st.write(f"Error communicating with Dialogflow: {e}")
