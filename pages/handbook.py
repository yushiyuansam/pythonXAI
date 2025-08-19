import streamlit as st

# Handbook：僅使用課程中已教過的語法與 st API

st.title("課程學習筆記（Handbook）")

import streamlit as st

# 單一且乾淨的 Handbook 實作，所有中文內容放在字串中
MD = """
# 課程學習筆記（Handbook）

## 目錄
- 基本型態
- 變數與賦值
- 運算子與優先順序
- 字串操作與格式化
- 型態檢查與轉換
- 長度與輸入範例
- List 與 CRUD 示範
- Streamlit 常用（僅列出已出現 API）
- 總結 / 下一步建議

---

## 1) 基本型態

示例：
```python
print(1)       # int
print(1.0)     # float
print('apple') # str
print(True)    # bool
```

## 2) 變數與賦值

使用 = 把右側的值存到左側變數：
```python
a = 10
b = 'apple'
```

## 3) 運算子與優先順序

常見運算子示例：
```python
1 + 1
1 - 1
1 * 1
1 / 2   # 小數除法
1 // 2  # 取商（整數除法）
3 % 2   # 取餘數
2 ** 3  # 次方
```

優先順序（由高到低）：括號、次方、乘除、加減

## 4) 字串操作與格式化

連接與重複：
```python
'Hello' + 'World'
'Hi' * 3
```

f-string 範例：
```python
name = 'apple'
age = 18
print(f"我的名字是{name}，我今年{age}歲")
```

## 5) 型態檢查與轉換

常用函式：
```python
len('apple')
type(1)
int(1.0)
float(1)
str(1)
bool(1)
```

## 6) 長度與輸入（input 範例）

終端機互動示例：
```python
a = input('請輸入一些文字:')
print(int(a) + 10)
```

Streamlit 範例（教材中已出現）：
```python
number = st.number_input('請輸入一個分數：', step=1, min_value=0, max_value=100)
st.write(f'你輸入的分數是：{number}')
```

## 7) List 與 CRUD 範例

```python
L = [1, 2, 3, 'a', 'b', 'c']
print(L[0])
print(L[1:4])
L[0] = 2
copy = L.copy()
L.remove('a')
L.pop()
```

## 8) Streamlit 已出現 API（教材中）

- st.title
- st.write
- st.text
- st.markdown
- st.number_input
- st.button
- st.balloons
- st.snow

範例：
```python
import streamlit as st
st.title('範例：Streamlit 元件')
number = st.number_input('請輸入一個數字：', step=1, min_value=0, max_value=100)
st.write(f'你輸入的數字是：{number}')
if st.button('按我一下', key='btn1'):
	st.balloons()
```

## 9) 小練習：計算圓面積

公式： area = 3.14 * r**2
```python
r = 2.0
area = 3.14 * r**2
print(area)
```

---

提醒：此筆記僅使用教材中已出現的語法與 API；未出現的語法（例如 def/class/try/except）暫不示範。
"""

st.title("課程學習筆記（Handbook）")
st.markdown(MD)
