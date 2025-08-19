import streamlit as st

# 使用 Streamlit 建立簡單互動介面
# st.number_input: 顯示數字輸入欄位，回傳使用者輸入的數值
#   - 第一個參數是顯示的提示文字
#   - step 指定調整步幅（整數情況下通常設為 1）
#   - min_value / max_value 限制輸入範圍
number = st.number_input("請輸入一個數字：", step=1, min_value=0, max_value=100)
st.write(f"你輸入的數字是：{number}")  # 顯示剛才輸入的數字

st.write("---")  # 在頁面上顯示分隔線

# 範例：輸入分數並依據分數顯示等級（A~E）
number = st.number_input("請輸入一個分數：", step=1, min_value=0, max_value=100)
st.write(f"你輸入的數字是：{number}")  # 顯示輸入的分數

# 使用 if / elif / else 進行範圍判斷
# 注意判斷順序：由高到低檢查能確保數值落在正確區間
if number >= 90:
    st.write("A")  # 90 以上為 A
elif number >= 80:
    st.write("B")  # 80-89 為 B
elif number >= 70:
    st.write("C")  # 70-79 為 C
elif number >= 60:
    st.write("D")  # 60-69 為 D
else:
    st.write("E")  # 0-59 為 E

st.write("---")
st.write("###按鈕練習")
st.button("按我一下", key="button1")
if st.button("按我一下", key="ballons"):
    st.balloons()  # 當按下按鈕時顯示氣球動畫

if st.button("按我一下", key="snow"):
    st.snow()  # 當按下按鈕時顯示下雪動畫（視 Streamlit 版本而定）
