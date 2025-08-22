import streamlit as st


ss = st.session_state

if "history" not in ss:
    ss.history = []

for message in ss.history:
    st.chat_message("user", avatar="👤").write(message["content"])

prompt = st.chat_input("請輸入訊息")
if prompt:
    ss.history.append({"role": "user", "content": prompt})
    st.rerun()
