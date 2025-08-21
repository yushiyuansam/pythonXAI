import streamlit as st
import random

# from streamlit import session_state as ss
import time

ss = st.session_state
# 使用 Streamlit 的 session_state 保存狀態，避免每次重新整理時變數消失
# session_state 可以用屬性方式存取，例如 ss.ans, ss.max_num, ss.min_num
if "ans" not in ss:  # 檢查 ans 是否已存在於 session_state 中
    # 隨機產生 1 到 100 的整數作為要猜的答案
    ss.ans = random.randint(1, 100)
if "max_num" not in ss:  # 檢查最大值是否存在於 session_state 中
    ss.max_num = 100  # 初始上界為 100
if "min_num" not in ss:  # 檢查最小值是否存在於 session_state 中
    ss.min_num = 1  # 初始下界為 1

st.title("猜數字遊戲")  # 在網頁上顯示標題

# number_input 讓使用者輸入整數；使用 f-string 顯示目前可輸入的範圍
num = st.number_input(f"請輸入{ss.min_num}~{ss.max_num}的整數：", step=1)

# 當使用者按下『猜中』按鈕時執行判斷
if st.button("猜中"):
    # 若輸入的數字比答案大，提示'太大了'，並調整上界
    if num > ss.ans:
        st.write("太大了")
        # 若猜的數字比目前上界小，則更新上界為猜的數字，縮小範圍
        if num < ss.max_num:
            ss.max_num = num
    # 若輸入的數字比答案小，提示'太小了'，並調整下界
    elif num < ss.ans:
        st.write("太小了")
        # 若猜的數字比目前下界大，則更新下界為猜的數字，縮小範圍
        if num > ss.min_num:
            ss.min_num = num
    # 猜中答案時顯示成功訊息並放氣球動畫
    else:
        st.write("答對了")
        st.balloons()

    # 暫停一秒鐘，讓使用者看見訊息，再重新整理頁面（rerun）以更新狀態與 UI
    time.sleep(1)
    st.rerun()
