import streamlit as st

# 主標題：點餐機
st.title("點餐機")

# 使用 session_state 儲存購物車資料（頁面重新整理時保留）
# 如果尚未建立 order，則建立一個空的 list
if "order" not in st.session_state:
    st.session_state.order = []

# 取出 session 中的 order 參考，後續透過 ss_order 直接修改
ss_order = st.session_state.order

# 使用兩欄版面呈現：左欄為輸入餐點，右欄為加入按鈕
col1, col2 = st.columns(2)
with col1:
    # text_input：讓使用者輸入餐點名稱（字串）
    dishes = st.text_input("請輸入餐點")
with col2:
    # 按下「加入」按鈕時，將輸入的餐點加入購物車
    if st.button("加入", key="add_order"):
        ss_order.append(dishes)


# 次標題：購物車（顯示已加入的餐點清單）
st.title("購物車")

# 逐項列出購物車的內容，並提供每一項的移除按鈕
# 注意：此處使用 index 作為按鈕 key，移除時會 pop 出該項並重新載入頁面
for i in range(len(ss_order)):
    col1, col2 = st.columns(2)
    with col1:
        # 顯示餐點名稱
        st.write(ss_order[i])
    with col2:
        # 每一列有對應的「移除」按鈕，按下會從 list 中刪除該項
        if st.button("移除", key=f"{i}"):
            ss_order.pop(i)
            # 刪除後重新執行應用，使畫面立即更新
            st.rerun()
