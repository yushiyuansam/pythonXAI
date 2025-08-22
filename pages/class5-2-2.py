import streamlit as st

st.chat_message("user").write("這是使用者的訊息")
st.chat_message("assistant").write("這是AI的回應")

history = [
    {"role": "user", "content": "你好,AI!"},
    {"role": "assistant", "content": "哈囉,你好!"},
    {"role": "user", "content": "我想問你一個問題!"},
    {"role": "assistant", "content": "好,請說!"},
]

for message in history:
    if message["role"] == "user":
        st.chat_message("user", avatar="👤").write(message["content"])
    else:
        st.chat_message("assistant", avatar="🤖").write(message["content"])
