import streamlit as st
import google.generativeai as genai
import os

# Configure Gemini Pro
API_KEY = st.secrets["GOOGLE_API_KEY"]  # We'll set this in Streamlit Cloud
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-pro')

# Page config
st.set_page_config(page_title="Friendly Chat", page_icon="💭")
st.title("Friendly Chat")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("What's on your mind?"):
    # Add user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate bot response
    chat = model.start_chat(history=[])
    system_prompt = """You are a friendly and supportive companion. Your main focus is to:
    1. Keep conversations focused on daily life and personal well-being
    2. Be empathetic and understanding
    3. Keep responses concise (under 50 words) and conversational
    4. If the conversation strays, gently guide it back to personal matters
    5. Be warm and authentic in your responses
    
    Remember to maintain a casual, friendly tone throughout the conversation."""
    
    response = chat.send_message(f"{system_prompt}\nUser: {prompt}")
    bot_response = response.text

    # Display bot response
    st.session_state.messages.append({"role": "assistant", "content": bot_response})
    with st.chat_message("assistant"):
        st.markdown(bot_response)