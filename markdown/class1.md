## 我學到的 Python 程式重點整理

## ✍️ 一、註解是什麼？

- 在程式前面加上 `#`，代表這一行是說明文字，電腦不會執行。

```python
# 這是一個註解
```

- 快速註解的方法：

  - 按下 `Ctrl + ?` 可以註解一行
  - 選取多行後按 `Ctrl + ?` 可以一次註解多行

---

## 🔢 二、基本資料型態（也就是資料的種類）

| 型態    | 說明             | 範例               |
| ------- | ---------------- | ------------------ |
| `int`   | 整數             | `1`, `-2`, `0`     |
| `float` | 小數             | `1.0`, `3.14`      |
| `str`   | 字串（文字）     | `"apple"`, `"123"` |
| `bool`  | 布林值（對或錯） | `True`, `False`    |

```python
print(1)        # 整數 int
print(1.0)      # 小數 float
print("apple")  # 字串 str
print(True)     # 布林值 bool
print(False)    # 布林值 bool
```

---

## 📦 三、變數（用來存東西的小盒子）

```python
a = "apple"  # 把"apple"放進a這個變數裡
a = 10       # 把數字10放進a裡（原本的值會被換掉）
```

- `=` 是「放進去」的意思，右邊的東西會被放到左邊的變數裡。

---

## ➕ 四、數學運算子（加減乘除）

| 運算     | 符號 | 範例     | 結果             |
| -------- | ---- | -------- | ---------------- |
| 加法     | `+`  | `1 + 2`  | 3                |
| 減法     | `-`  | `5 - 3`  | 2                |
| 乘法     | `*`  | `2 * 3`  | 6                |
| 除法     | `/`  | `4 / 2`  | 2.0（小數）      |
| 整數除法 | `//` | `5 // 2` | 2（只取商）      |
| 餘數     | `%`  | `5 % 2`  | 1（只取餘數）    |
| 次方     | `**` | `2 ** 3` | 8（2 的 3 次方） |

💡 運算的優先順序（先做誰？）：

1. 括號 ()
2. 次方 \*\*
3. 乘除 \* /
4. 加減 + -

---

## 🧵 五、字串運算（文字的加法和乘法）

```python
print("Hello" + "World")  # 變成 HelloWorld
print("Hi" * 3)           # 變成 HiHiHi
```

---

## 🧑‍💻 六、f-string：把變數放進句子裡

```python
name = "apple"
age = 18
print(f"我是{name}，我今年{age}歲")
```

➡️ 用 `f""` 字串可以把變數放進去，用 `{}` 包起來就可以顯示。

---

## 🔢 七、len() 和 type()

- `len()`：看字串有幾個字。

```python
print(len("apple"))  # 5
```

- `type()`：看變數是什麼型態。

```python
print(type(1))       # int
print(type(1.0))     # float
print(type("apple")) # str
print(type(True))    # bool
```

---

## 🔄 八、型態轉換（換資料的種類）

```python
print(int(1.0))    # float 變 int → 1
print(float(1))    # int 變 float → 1.0
print(str(1))      # int 變 str → "1"
print(bool(1))     # int 變 bool → True
```

⚠️ 注意：不是所有東西都能轉，比如：

```python
int("hello")  # 會出錯，因為 "hello" 不能變成數字
```

---

## ⌨️ 九、input()：讓使用者輸入東西

```python
a = input("請輸入一些文字:")  # 會跳出提示讓你輸入
print(a)
```

- 使用者輸入的東西**都是字串**！
- 如果想拿來算數學，要先轉成整數：

```python
print(int(a) + 10)
```

---

## 🧮 十、計算圓面積（綜合練習）

```python
r = input("請輸入圓的半徑:")
r = float(r)
area = 3.14 * r ** 2
print(area)
```

---

## 🌐 十一、Streamlit 的基本使用（做網站的工具）

```python
import streamlit as st

st.title("這是標題")  # 顯示大標題
st.write("這是一段文字")  # 顯示內容（支援很多格式）
st.text("這是純文字")     # 顯示純文字
```

---

## 📝 十二、Markdown 語法（讓文字變漂亮）

```markdown
# 這是最大標題

## 這是第二大標題

### 這是第三大標題

- **粗體文字**
- _斜體文字_
- [這是一個連結](https://www.example.com)
```

---

## 🎉 我已經學會了這些程式技巧！

✅ 基本資料型態
✅ 加減乘除運算
✅ 字串和變數
✅ 輸入與輸出
✅ 型態轉換
✅ 使用 `len()` 和 `type()`
✅ f-string
✅ Streamlit 的基本用法
