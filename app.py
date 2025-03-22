import streamlit as st
import google.generativeai as genai

# --- Configuration ---
API_KEY = "AIzaSyBD409CWUKxgOeEVtbFMhoLD_ELweuyZzk"  # Replace with your actual API key
genai.configure(api_key=API_KEY)

# Load Gemini Pro model
model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest")

# --- Streamlit Page Settings ---
st.set_page_config(page_title="Friendly Chat", page_icon="💭")
st.title("Friendly Chat")

# --- Initialize Chat History ---
if "messages" not in st.session_state:
    st.session_state.messages = []
    # Initial greeting from assistant
    system_greeting = "Hi there! How are you feeling today? 😊"
    st.session_state.messages.append({"role": "assistant", "content": system_greeting})

# --- Display Chat Messages ---
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# --- Handle User Input ---
if prompt := st.chat_input("Share your thoughts..."):
    # Save user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Create conversation history for context
    conversation_history = "\n".join([
        f"{'User' if msg['role'] == 'user' else 'Assistant'}: {msg['content']}"
        for msg in st.session_state.messages[:-1]  # Exclude current user message
    ])

    # System prompt for Gemini
    system_prompt = f"""
You are a mature and sophisticated friend having a deeply engaging conversation. Key attributes:

Personality:
- Highly empathetic and emotionally intelligent
- Thoughtful and insightful in responses
- Maintains perfect context awareness
- Adapts tone to match the emotional depth of conversation

Conversation Mastery:
- Give concise but meaningful responses (2-3 sentences)
- Ask thoughtful follow-up questions that show deep understanding
- Reference previous parts of the conversation naturally
- Maintain consistent personality throughout

Advanced Guidelines:
- Build upon previous exchanges to deepen the connection
- Show genuine curiosity about the user's experiences
- Gently explore deeper if user gives brief responses
- Keep the conversation flowing naturally like a close friend
- Never be repetitive or generic

Previous Conversation:
{conversation_history}

User: {prompt}
"""

    # --- Generate Gemini Response ---
    try:
        response = model.generate_content(system_prompt)
        bot_response = response.text
    except Exception as e:
        bot_response = f"⚠️ Error: {e}"

    # Display Gemini's reply
    st.session_state.messages.append({"role": "assistant", "content": bot_response})
    with st.chat_message("assistant"):
        st.markdown(bot_response)
