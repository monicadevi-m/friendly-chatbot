import streamlit as st
import pandas as pd
from datetime import datetime

def export_chat_history():
    if not st.session_state.messages:
        st.warning("No messages to export!")
        return
        
    chat_data = []
    for msg in st.session_state.messages:
        chat_data.append({
            'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'role': msg['role'],
            'content': msg['content']
        })
    
    df = pd.DataFrame(chat_data)
    filename = f'chat_history_{datetime.now().strftime("%Y%m%d_%H%M%S")}.xlsx'
    df.to_excel(filename, index=False)
    return filename