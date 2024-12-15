import streamlit as st
import pandas as pd

def view_chat_history():
    st.title("Chat History Viewer")
    
    try:
        import glob
        files = glob.glob('chat_history_*.xlsx')
        
        if files:
            selected_file = st.selectbox('Select chat history file:', files)
            df = pd.read_excel(selected_file)
            st.dataframe(df)
        else:
            st.info("No chat history files found")
    except Exception as e:
        st.error(f"Error loading chat history: {e}")

if __name__ == "__main__":
    view_chat_history()