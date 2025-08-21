## 🧠 我學到的程式指令整理

### 🧩 字典 dict

- 字典就像一個資料盒子，用「名字（key）」來找「資料（value）」。
- 一個名字只能對應一個資料，但資料可以重複。
- 字典裡的東西沒有順序，不能用第幾個來找，只能用名字找。
- 名字要是不能改的東西，比如：數字、文字。
- 寫法：

  ```python
  d = {"a": 1, "b": 2, "c": 3}
  ```

#### 讀取資料（查資料）

```python
print(d["a"])  # 印出1
```

#### 拿出所有的 key（名字）

```python
print(d.keys())
for key in d.keys():
    print(key)
```

#### 拿出所有的 value（資料）

```python
print(d.values())
for value in d.values():
    print(value)
```

#### 拿出所有的 key 和 value

```python
print(d.items())
for key, value in d.items():
    print(key, value)
```

#### 新增或修改資料

```python
d["d"] = 4  # 新增
d["a"] = 5  # 修改
```

#### 刪除資料

```python
d.pop("a")  # 刪掉"a"
d.pop("e", "Not Found")  # 如果沒有這個key，就顯示"Not Found"
```

#### 其他指令

```python
print(len(d))        # 看字典有幾組資料
print("a" in d)      # 檢查"a"有沒有在字典裡（只能查key）
```

---

## 🖼️ 顯示圖片的程式

使用 `streamlit` 套件可以讓程式變成網頁，像是在做網站！

### 顯示單張圖片

```python
st.image("image/狗子.png", width=400)
```

### 顯示整個資料夾的圖片

```python
image_files = os.listdir("image")  # 把image資料夾裡的檔案名稱全部拿出來
for image_file in image_files:
    st.image(f"image/{image_file}", width=image_size)
```

### 使用者可以選擇圖片大小

```python
image_size = st.number_input("圖片大小", min_value=50, max_value=800, step=50, value=200)
```

### 做下拉式選單選圖片

```python
selected_image = st.selectbox("選擇圖片", image_files, index=0)
st.image(f"image/{selected_image}", width=400)
```

---

## 🛒 購物平台程式（小型購物網站）

### 商品資料怎麼存？

用 `字典` 把每個商品的名字、價格、庫存和圖片記錄下來：

```python
ss.products = {
    "apple": {"price": 10, "stock": 10, "image": "image/apple.png"},
    "banana": {"price": 10, "stock": 10, "image": "image/banana.png"},
}
```

### 顯示每個商品（3 欄排版）

```python
cols = st.columns(3)
for product_name, detales in ss.products.items():
    st.image(detales["image"], use_container_width=True)
    st.write(f"### {product_name}")
    st.write(f"價格:{detales['price']}")
    st.write(f"庫存:{detales['stock']}")
```

### 購買商品（按鈕）

```python
if st.button(f"購買 {product_name}", key=f"{product_name}"):
    if detales["stock"] > 0:
        ss.products[product_name]["stock"] -= 1
    st.rerun()
```

### 新增庫存（補貨功能）

```python
selected_product = st.selectbox("選擇商品", ss.products.keys())
new_stock = st.number_input("新增庫存數量", min_value=1, step=1)
if st.button("補獲"):
    ss.products[selected_product]["stock"] += new_stock
    st.rerun()
```

---

## 🔧 函數 function

### 沒有參數的函數

```python
def hello():
    print("Hello World")
```

### 有參數的函數

```python
def hello(name):
    print(f"Hello {name}")

hello("Alice")
hello("Bob")
```

### 有回傳值的函數（可以回傳多個值）

```python
def add_sub(a, b):
    return a + b, a - b

sum, sub = add_sub(5, 6)
print(f"sum={sum}, sub={sub}")
```

### 回傳不同結果的函數

```python
def add_sub(a, b):
    if a > b:
        return a + b
    else:
        return a - b
```
