import streamlit as st
from main import chat_with_gpt as chat

st.title("Physics HW")

sysmes = "You are a highly capable, proactive AI agent designed to autonomously complete complex tasks for users. Answer this question: "
if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []

st.session_state["submit"] = False

def on_change():
    st.session_state["submit"] = True


user_input = st.text_input("You:", key="user_input", on_change=on_change)

if st.button("Send") and user_input:
    "Give it a second"
    response = chat(f"{sysmes} {user_input}")
    response