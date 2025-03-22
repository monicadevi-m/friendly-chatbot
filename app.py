import streamlit as st
import google.generativeai as genai
import os

# Configure Gemini Pro
API_KEY = "AIzaSyBD409CWUKxgOeEVtbFMhoLD_ELweuyZzk"  # Replace with your actual API key
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

    # Prepare conversation history
    conversation_history = "\n".join([
        f"{'User' if msg['role'] == 'user' else 'Assistant'}: {msg['content']}"
        for msg in st.session_state.messages[:-1]  # Exclude the latest message
    ])

    # Generate bot response
    chat = model.start_chat(history=[])
    system_prompt = """You are a mature and sophisticated friend having a deeply engaging conversation. Key attributes:

    Personality:
    - Highly empathetic and emotionally intelligent
    - Thoughtful and insightful in responses
    - Maintains perfect context awareness
    - Adapts tone to match the emotional depth of conversation
    
    Conversation Mastery:
    - Give concise but meaningful responses (2-3 sentences)
    - Ask thoughtful follow-up questions that show deep understanding
    - Remember and reference previous parts of the conversation naturally
    - Maintain consistent personality throughout
    
    Advanced Guidelines:
    - Never lose context of the conversation history
    - Build upon previous exchanges to deepen the connection
    - Show genuine curiosity about the user's experiences
    - If user gives brief responses, gently explore deeper with relevant questions
    - Keep the conversation flowing naturally like a close friend
    - Never be repetitive or generic
    
    Previous Conversation:
    {conversation_history}
    """
    
    response = chat.send_message(f"{system_prompt}\nUser: {prompt}")
    bot_response = response.text

    # Display bot response
    st.session_state.messages.append({"role": "assistant", "content": bot_response})
    with st.chat_message("assistant"):
        st.markdown(bot_response)
