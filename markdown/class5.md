# 🖥️ 我的程式學習重點整理

## 一、函數的預設值

### ✅ 函數可以有「預設的參數」

- 當我在呼叫函數的時候，如果我沒有給某個參數，電腦就會用預設的值。

```python
def hello(name, message="Hello"):
    print(f"{message},{name}!")
```

✅ 呼叫方式：

```python
hello("Alice")         # 印出 Hello,Alice!
hello("Bob", "早安")   # 印出 早安,Bob!
```

📝 **小提醒**：有預設值的要放在後面，沒預設值的要放前面。

---

## 二、限制參數的類型

### ✅ 可以告訴電腦「這個參數應該是什麼類型」

```python
def add(a: int, b: int = 0) -> int:
    return a + b
```

這代表：

- `a` 和 `b` 要是數字（int）
- 最後會回傳一個數字

---

## 三、區域變數 和 全域變數

### ✅ 區域變數：只在函數裡面有用

### ✅ 全域變數：在整個程式都可以用

```python
length = 5  # 全域變數

def calculate_square_area():
    area = length**2  # area是區域變數
    print("面積是", area)
```

📝 注意：如果在函數裡要修改全域變數，要加上 `global`

```python
def calculate_square_area():
    global area
    area = length**2
```

---

## 四、函數的說明

### ✅ 可以在函數裡面加上說明文字

```python
def hello(name: str):
    """
    這是一個打招呼的函數
    傳入：名字（name）
    回傳：沒有
    """
    print(f"Hello,{name}!")
```

這樣別人看你的程式時，就知道這個函數是做什麼的！

---

## 五、使用 OpenAI API 和環境變數

### ✅ 學會了怎麼使用 `.env` 檔來保護金鑰（API key）

```python
import openai
from dotenv import load_dotenv
import os

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
```

---

## 六、做出一個簡單的聊天機器人

### ✅ 使用 while 迴圈和 history 來記錄對話

```python
while True:
    user_input = input("你:")
    if user_input == "exit":
        break
```

### ✅ 用 OpenAI API 回答問題

```python
response = openai.chat.completions.create(
    model="gpt-5-mini",
    messages=history,
)
```

---

## 七、使用 Streamlit 做出網頁聊天介面

### ✅ 學會用 `streamlit` 顯示聊天內容

```python
import streamlit as st

if "history" not in st.session_state:
    st.session_state.history = []
```

### ✅ 用按鈕刪除聊天紀錄

```python
if st.button("🗑️"):
    st.session_state.history = [{"role": "system", "content": "請用繁體中文進行後續對話"}]
    st.rerun()
```

---

## 八、我學會的觀念總整理 🧠

- 函數可以設定預設值，讓程式更有彈性
- 可以設定參數和回傳值的類型
- 要注意變數的範圍（區域 vs 全域）
- 函數可以加說明文字，讓程式更清楚
- 學會使用 `.env` 保護機密資訊
- 知道怎麼用 OpenAI API 跟聊天機器人對話
- 學會用 Streamlit 做網頁版的聊天室
