import streamlit as st

# 標題：示範欄位（columns）元件的使用方式
st.title("欄位元件")

# 建立兩等分的欄位佈局，分別在兩側放置按鈕
col1, col2 = st.columns(2)
col1.button("按鈕1", key="btn1")  # 左側按鈕
col2.button("按鈕2", key="btn2")  # 右側按鈕

# 使用不同權重建立欄位（左:右 = 1:2），觀察寬度差異
col1, col2 = st.columns([1, 2])
col1.button("按鈕3", key="btn3")
col2.button("按鈕4", key="btn4")

# 三欄位示範，設定寬度比為 1:2:3
col1, col2, col3 = st.columns([1, 2, 3])
col1.button("按鈕5", key="btn5")
col2.button("按鈕6", key="btn6")
col3.button("按鈕7", key="btn7")
st.write("---")  # 分隔線

# 在欄位內使用 with 區塊來放置多個元件
col1, col2 = st.columns([1, 2])
with col1:
    st.write("這是col1")
    # 如果按下按鈕，觸發氣球動畫表示互動
    if st.button("按鈕8", key="btn8"):
        st.balloons()
with col2:
    st.write("這是col2")
    st.button("按鈕9", key="btn9")

# 動態建立指定數量的欄位，透過 number_input 讓使用者輸入欄位數
n = st.number_input("請輸入欄位數", min_value=1, value=4, step=1)
cols = st.columns(n)  # 根據輸入建立 n 個欄位物件的 list
for i in range(len(cols)):
    # 在每個欄位中放置一個按鈕，key 要唯一以避免衝突
    with cols[i]:
        st.button(f"按鈕{i+1}", key=f"多col{i+10}")
st.write("---")

# 比較不同排列方式對元件顯示的影響（標題說明）
st.title("coiumnsq排列元件效果比較")
col1, col2 = st.columns(2)
with col1:
    # 在同一欄位堆疊多個按鈕，觀察垂直排列效果
    st.button("按鈕1", key="btn10")
    st.button("按鈕2", key="btn11")
    st.button("按鈕3", key="btn12")
with col2:
    # 在另一欄放多個文字，觀察垂直文字排列
    st.write("這是col2")
    st.write("這是col2")
    st.write("這是col2")
st.write("---")

# 使用迴圈每一列建立兩欄，測試排版一致性
for i in range(3):
    col1, col2 = st.columns(2)
    with col1:
        st.button(f"按鈕{i+1}", key=f"排版測試{i+4}")
    with col2:
        st.write(f"這是col2_{i+1}")

st.write("---")

# 範例：示範 session_state 的基本用法
st.title("session_state")
# 注意：直接用區域變數 ans 無法跨 rerun 保留狀態，下面示範兩種寫法
ans = 1
# 這個按鈕每次 rerun 都會重設 ans（因為 ans 是區域變數）
if st.button("按下去ans加1", key="btn_ans"):
    ans = ans + 1
st.write(f"ans={ans}")  # 會顯示當前 rerun 的區域變數值

# 正確做法：使用 st.session_state 來保存跨 rerun 的狀態
if "ans" not in st.session_state:
    st.session_state.ans = 1  # 初始化 session_state 變數

if st.button("按下去ans加1", key="btn_ans2"):
    st.session_state.ans = st.session_state.ans + 1
st.write(f"ans={st.session_state.ans}")  # 顯示儲存在 session_state 的值

# 提供一個觸發重新整理 (rerun) 的按鈕
if st.button("重新整理畫面", key="banana"):
    st.rerun()
