# def
# 新增一個函數函數要用def開頭,後面接著函數名稱,再加上小括號,最後加上冒號
# 小括號裡面可以放入傳入函數的參數也可以不放
def hello():
    print("Hello World")


for i in range(10):
    hello()


# 有傳入參數的函數
# 這個函數有一個參數 name,當呼叫這個函數時,可以傳入一筆資料給 name
def hello(name):
    print(f"Hello {name}")


hello("Alice")
hello("Bob")
hello("Charlie")
for i in range(10):
    hello(i)  # 這樣的i會被當作name的值


# 有多個回傳值的函數
# 這是函數會回傳兩個值,當呼叫這個函數時,可以把回傳值存起來
def add_sub(a, b):
    return a + b, a - b


sum, sub = add_sub(5, 6)  # 可以將回傳值存到多個變數中
print(f"sum={sum},sub={sub}")


# 多個return
def add_sub(a, b):
    if a > b:
        return a + b
    else:
        return a - b


print(add_sub(5, 6))
print(add_sub(6, 5))
