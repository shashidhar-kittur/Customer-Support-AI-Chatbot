import streamlit as st
import requests

st.title("AI Support Bot")
session_id = st.text_input("Session ID", "default")
query = st.text_input("Your query")
if st.button("Send"):
    response = requests.post("http://localhost:8000/chat", json={"session_id": session_id, "query": query}).json()
    
    st.write(response['response'])
    if response['escalate']:
        st.write("Escalated! Summary: " + response['summary'])