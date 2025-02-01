import streamlit as st
import requests

# Set up the FastAPI server URL
API_URL = "https://securecodebot.onrender.com/chat"

# Streamlit interface
st.title("Chatbot Application")

# Display a text input for the user question
user_question = st.text_input("Ask a question:")

if user_question:
    # Send the user's question to the FastAPI backend
    response = requests.post(API_URL, json={"question": user_question})
    
    if response.status_code == 200:
        # Display the chatbot's response
        bot_answer = response.json().get("answer")
        st.write("Bot:", bot_answer)
    else:
        st.error("Error communicating with the API.")
