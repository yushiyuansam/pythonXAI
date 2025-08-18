import streamlit as st

st.title("這是標題")
st.write("這是一個用 `st.write` 顯示的字串，可以處理多種格式，例如：數字、文字、Markdown、數據框等。")
st.text("這是一個用 `st.text` 顯示的純文字字串，只能顯示純文字，不支持其他格式。")
st.markdown(
    """
這是一個用 `st.markdown` 顯示的字串，可以處理 Markdown 語法。
例如：
* **粗體文字**
* *斜體文字*
* [連結](https://www.example.com)
* 代碼塊：
```python
print("Hello, Streamlit!")
```
"""
)


st.write(
    """
# 這是最大標題

- 這是第一個項目
- 這是第二個項目
- 這是第三個項目

## 這是第二大標題

```python
print("Hello World!")
```

### 這是第三大標題
- 這是第一個項目
    - 這是第一個子項目
    - 這是第二個子項目
---

#### 這是第四大標題

---

##### 這是第五大標題

---

###### 這是第六大標題

"""
)