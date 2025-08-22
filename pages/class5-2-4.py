import streamlit as st
import openai

openai.api_key = st.secrets["OPENAI_API_KEY"]
ss = st.session_state
if "history" not in ss:
    ss.history = [{"role": "system", "content": f"請用繁體中文進行後續對話"}]
col_chat, col_clear = st.columns([9, 1])
with col_clear:
    # 新增刪除對話紀錄按鈕,按鈕上的文字不需要直接用emoji
    if st.button("🗑️"):
        ss.history = [{"role": "system", "content": f"請用繁體中文進行後續對話"}]
        st.rerun()

with col_chat:
    for message in ss.history:
        if message["role"] == "user":
            st.chat_message("user", avatar="👤").write(message["content"])
        if message["role"] == "assistant":
            st.chat_message("assistant", avatar="🤖").write(message["content"])

prompt = st.chat_input("請輸入訊息")
if prompt:
    ss.history.append({"role": "user", "content": prompt})

    response = openai.chat.completions.create(
        model="gpt-5",
        messages=ss.history,
    )

    assistant_message = response.choices[0].message.content
    ss.history.append({"role": "assistant", "content": assistant_message})
    st.rerun()
