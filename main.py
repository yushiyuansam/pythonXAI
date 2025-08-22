import streamlit as st

st.set_page_config(page_title="SamPython XAI", page_icon="🐍", layout="wide")

all_pages = {
    "": [
        st.Page("pages/home.py", title="🏠首頁"),
        st.Page("pages/handbook.py", title="🗒️課程筆記"),
    ],
    "📚程式練習": [
        st.Page("pages/class1-2.py", title="markdown語法"),
        st.Page("pages/class2-2.py", title="💯成績評分"),
        st.Page("pages/class2-4.py", title="🔢數學金字塔"),
        st.Page("pages/class3-1.py", title="👀column與session_state"),
        st.Page("pages/class3-2.py", title="🥖🥞🥕點餐機"),
        st.Page("pages/class3-5.py", title="❓猜數字遊戲"),
        st.Page("pages/class4-2.py", title="🚗圖片練習"),
        st.Page("pages/class4-3.py", title="💵💶💷購頻平台"),
        st.Page("pages/class5-2-2.py", title="🤖💬聊天泡泡"),
        st.Page("pages/class5-2-3.py", title="💬🗨️聊天輸入框"),
        st.Page("pages/class5-2-4.py", title="🔑🔐AI聊天機器人"),
    ],
}

nav = st.navigation(all_pages, position="sidebar")
nav.run()
