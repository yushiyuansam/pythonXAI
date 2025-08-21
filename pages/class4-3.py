import streamlit as st
import os

st.title("購物平台")  # 顯示網頁標題
ss = st.session_state  # 簡短變數，方便使用 session_state

# 設定圖片資料夾名稱，並讀取資料夾內所有檔案名稱
image_folder = "image"
image_files = os.listdir(image_folder)  # 讀取 image 資料夾內的所有檔案

# 使用 session_state 保存商品資料，避免每次重新整理後資料遺失
if "products" not in ss:
    ss.products = {}  # 建立 products 字典，用來儲存所有商品資訊

# 根據 image 資料夾中的檔案建立初始商品資料（若尚未存在於 ss.products）
for image_file in image_files:
    # 假設檔名格式為 'apple.png'，去掉副檔名取得商品名稱
    product_name = image_file[:-4]
    if product_name not in ss.products:  # 如果商品不存在，則新增商品資料
        ss.products[product_name] = {
            "price": 10,  # 預設價格為 10
            "stock": 10,  # 預設庫存為 10
            "image": f"{image_folder}/{image_file}",  # 圖片路徑
        }

# 將商品以 3 欄方式顯示在畫面上
cols = st.columns(3)
i = 0
for product_name, detales in ss.products.items():
    # product_name 裡面是商品名稱，detales 裡面是商品詳細資訊的字典
    # 例如: {"price":10, "stock":10, "image":"image/apple.png"}
    with cols[i % len(cols)]:
        # 顯示商品圖片（自動填滿容器寬度）和名稱、價格、庫存
        st.image(detales["image"], use_container_width=True)
        st.write(f"### {product_name}")
        st.write(f"價格:{detales['price']}")
        st.write(f"庫存:{detales['stock']}")

        # 每個商品都有一個購買按鈕，按下後若有庫存則庫存減 1
        if st.button(f"購買 {product_name}", key=f"{product_name}"):
            if detales["stock"] > 0:
                ss.products[product_name]["stock"] -= 1  # 庫存扣除
            st.rerun()  # 按下按鈕後重新整理頁面以更新 UI
        i += 1


# --- 新增商品庫存區域 ---
st.title("新增商品庫存")
col1, col2, col3 = st.columns(3)
with col1:
    # 選擇要補貨的商品，選項來自 ss.products 的鍵（也就是商品名稱）
    selected_product = st.selectbox("選擇商品", ss.products.keys())
with col2:
    # 輸入要新增的庫存數量，最小為 1
    new_stock = st.number_input("新增庫存數量", min_value=1, step=1)
with col3:
    # 補貨按鈕，按下後將選定商品的庫存增加輸入的數量
    if st.button("補獲"):
        ss.products[selected_product]["stock"] += new_stock
        st.rerun()


# ss.products 範例（註解示範如何存取資料）
# ss.products={"apple":{"price":10,"stock":10,"image":"image/apple.png"},
#           "banana":{"price":10,"stock":10,"image":"image/banana.png"},
#           "orange":{"price":10,"stock":10,"image":"image/orange.png"}
# }
# 如何找到蘋果的價格? ss.products["apple"]["price"]
# 如何找到香蕉的庫存? ss.products["banana"]["stock"]
# 如何找到橘子的圖片? ss.products["orange"]["image"]
