import streamlit as st

# 小學生友善的程式教學總整理（只用你學過的指令）
st.title("程式小教室：今天學到的重點")

# 簡短導言
st.write(
	"這裡把今天在課堂上學到的重要觀念整理成短短幾點，語句簡單，方便複習。"
)


st.markdown("""
## 1) 基本型態（想像不同的東西）

- 整數 (int)：例如 1, 2, 3
- 浮點數 (float)：例如 1.0, 2.5
- 字串 (str)：例如 'apple'
- 布林 (bool)：True 或 False
""")


st.markdown("""
## 2) 變數：把東西放到盒子裡

用 = 把值放到變數裡，例如：

```
a = 10
b = 'apple'
```
""")


st.markdown("""
## 3) 常用數學運算

- 加、減、乘、除、整數除、餘數、次方

範例：
```
1 + 1
1 - 1
1 * 1
1 / 2   # 會得到小數
1 // 2  # 只要商
3 % 2   # 取餘數
2 ** 3  # 次方
```
""")


st.markdown("""
## 4) 字串的簡單用法

- 字串可以連接（相加）或重複（乘法）：
```
'Hello' + 'World'  # 'HelloWorld'
'Hi' * 3           # 'HiHiHi'
```
""")


st.markdown("""
## 5) 把變數放進字串（f-string）

範例：
```
name = 'apple'
age = 18
print(f"我的名字是{name}，我今年{age}歲")
```
""")


st.markdown("""
## 6) 檢查長度與型態

- len()：計算長度
- type()：看是什麼型態

```
len('apple')  # 5
type(1)       # int
```
""")


st.markdown("""
## 7) 型態轉換（把東西換成別的型態）

常見有 int, float, str, bool，例如：
```
int(1.0)
float(1)
str(1)
bool(0)
```
""")


st.markdown("""
## 8) input() 的示意（在終端機使用）

課堂上有看到 input()，它會讓使用者在終端機輸入文字：
```
a = input('請輸入一些文字:')
print(int(a) + 10)
```
在 Streamlit 我們不會用 input()，所以這裡只當示意。""")


st.markdown("""
## 9) 小練習：計算圓面積（示範）

公式： area = 3.14 * r**2

```
r = 2.0
area = 3.14 * r**2
print(area)
```
""")


st.markdown("""
---

提醒：這份教學只用了你已學過的內容。不要使用還沒學過的進階指令或模組。
""")


st.markdown("""
## 總結

今天我們學了：基本型態、變數、運算、字串、型別檢查與轉換、簡單小練習。
多練習會更熟！
""")
