import streamlit as st
import google.generativeai as genai
import os

# Configure Gemini Pro
API_KEY = "AIzaSyBqN8pjV5DScFN2sYlxeBmAiA0wwuvj6OI"  # Replace with your actual API key
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-pro')

# Page config
st.set_page_config(page_title="Friendly Chat", page_icon="💭")
st.title("Friendly Chat")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []
    # Add initial greeting
    system_greeting = "Hi there! How are you feeling today? 😊"
    st.session_state.messages.append({"role": "assistant", "content": system_greeting})

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("Share your thoughts..."):
    # Add user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate bot response
    chat = model.start_chat(history=[])
    system_prompt = """You are a mature, empathetic friend who:
    - Listens attentively and responds thoughtfully
    - Shows genuine interest in the person's feelings and experiences
    - Offers gentle support and understanding
    - Maintains natural, flowing conversations
    - Shares relevant insights when appropriate
    - Keeps responses concise but meaningful
    
    Remember to be authentic and warm, like a close friend having a genuine conversation."""
    
    response = chat.send_message(f"{system_prompt}\nUser: {prompt}")
    bot_response = response.text

    # Display bot response
    st.session_state.messages.append({"role": "assistant", "content": bot_response})
    with st.chat_message("assistant"):
        st.markdown(bot_response)
