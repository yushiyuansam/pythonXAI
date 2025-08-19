# 這是 Streamlit 範例：示範如何使用 number_input 與簡單的 for 迴圈輸出
# 註解風格參考 class1-1.py：以中文說明每個區塊的用途與參數
import streamlit as st

# number_input：讓使用者在網頁上輸入一個整數（此範例為 1-9）
# step=1 表示每次遞增 1；min_value 與 max_value 限定輸入範圍
number = st.number_input("請輸入一個分數：", step=1, min_value=1, max_value=9)

# for 迴圈：從 1 到使用者輸入的數字 (包含該數字)
# 迴圈內使用 f-string 與字串乘法來產生簡單的圖形化輸出
for i in range(1, number + 1):
    # f"{i}" * i 會先把數字 i 轉成字串，然後重複 i 次，
    # 例如 i=3 則輸出 "333"；此處使用 st.write 顯示在 Streamlit 頁面
    st.write(f"{i}" * i)
