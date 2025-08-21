import streamlit as st
import os

st.title("圖片元件")
# st.image指令,參數(圖片2;304路徑,寬度)
st.image("image/狗子.png", width=400)

image_folder = "image"  # 檔案夾名稱
image_files = os.listdir(image_folder)  # 取得檔案夾內所有檔案
st.write(image_files)  # 顯示所有檔案
image_size = st.number_input(
    "圖片大小", min_value=50, max_value=800, step=50, value=200
)
# 使用者輸入圖片大小,最小50, 最大800, 預設200步,每次增加50
for image_file in image_files:  # 顯示所有圖片
    st.image(f"{image_folder}/{image_file}", width=image_size)
# 顯示圖片,根據使用者輸入的大小調整寬度
for image_file in image_files:  # 顯示所有圖片
    # 除了width,還有use_container_width可以使用,會將圖片寬度設為容器寬度
    st.image(f"{image_folder}/{image_file}", width=image_size)
    # 顯示圖片,使用容器寬度

# selectbox選擇圖片
selected_image = st.selectbox("選擇圖片", image_files, index=0)  # 下拉是選單選擇圖片
st.image(f"{image_folder}/{selected_image}", width=400)  # 顯示選擇的圖片
