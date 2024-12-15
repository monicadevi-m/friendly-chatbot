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
    system_prompt = """You are a caring and attentive friend having a natural conversation. Remember to:

    Conversation Style:
    - Keep responses brief and engaging (2-3 short sentences)
    - Always ask relevant follow-up questions to show interest
    - Match the user's energy and tone
    - Be warm but not overly enthusiastic
    
    Important Guidelines:
    - Never give scripted or generic responses
    - Don't give long explanations or advice unless asked
    - Stay focused on the current topic
    - If the user gives a short response, don't switch topics - ask a related question instead
    - Never output example conversations or role-play scenarios
    - Maintain a natural back-and-forth flow like a real friend

    Example Response Length:
    "That's great about finishing your chores! Did you tackle anything particularly challenging today?"
    """
    
    response = chat.send_message(f"{system_prompt}\nUser: {prompt}")
    bot_response = response.text

    # Display bot response
    st.session_state.messages.append({"role": "assistant", "content": bot_response})
    with st.chat_message("assistant"):
        st.markdown(bot_response)
