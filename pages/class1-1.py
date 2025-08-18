# 這是註解，不會被執行
# Ctrl +? 可以把單行程式註解起來
#如果框選多行程式碼，Ctrl +  ? 可以把多行程式碼註解起來

# 基本型態
print(1)  #int這是整數,-1,0,1,2,3,4,5,6,7,8,9
print(1.0) #(1.0)  #float這是浮點數
print("apple") #str這是字串"sadasd123125557","1"
print("1") #bool這是布林值True,False,對或錯
print(True)  #bool這是布林值True,False,對或錯
print(False)  #bool這是布林值True,False,對或錯



# 變數
a="apple" #在終端機顯示所存的值
a=10 #新增一個存儲空間a，"="的功能是把右邊的值存到左邊的變數
a="apple" #如果a已經有值了，這個值會被覆蓋

# 運算子
print(1+1)  #加法
print(1-1)  #減法
print(1*1)  #乘法
print(1/1)  #除法(小數除法2.4=2.4)
print(1//2)  #整數除法(取商2.4=2)
print(1%2)  #取餘數(2.4=3)
print(2**3)  #乘方(2的3次方=8)

# 優先順序
# 1. 括號
# 2. 次方
# 3. 乘除
# 4. 加減

# 請用前面的用詞標準來完成以下的程式碼的註解

# 字串運算,+、*
print("Hello" + "World")  # 字串連接
print("Hello" * 3)  # 字串乘法

# 字串格式化
name="apple" #字串變數
age=18 #整數變數
print(f"我的名字是{name}，我今年{age}歲")  # 使用f-string格式化字串 
# 可以將變數或其他型態的資料放到f字串中裡面的{}, 這樣可以在字串中顯示

# len()函式可以計算字串的長度
print(len("apple"))  # 計算字串長度，結果是5

# tpye() #函式可以檢查變數的型態
print (type(1)) #<class 'int'>  # 檢查變數的型態，結果是整數
print(type(1.0))  # <class 'float'>  # 檢查變數的型態，結果是浮點數
print(type("apple"))  # <class 'str'>  # 檢查變數的型態，結果是字串
print(type(True))  # <class 'bool'>  # 檢查變數的型態，結果是布林值

# 型態轉換
print(int(1.0)) #float轉int
print(float(1)) #int轉float
print(str(1)) #int轉str
print(bool(1)) #int轉bool
print(int(1.234)) #float轉int
print(float(1.234)) #str轉float
print(str(1.234)) #float轉str
print(bool(1.234)) #float轉bool
# print(int("hello"))   #這會報錯，因為"hello"不能轉成整數

print("輸入開始")
# input()函式可以讓使用者輸入資料
# ()裡面的文字試題是訊息會顯示在終端機上，提示使用者輸入
a=input("請輸入一些文字:")
print("輸入結束")
print(int(a)+10)
print(int(a)) #證明透過input()輸入內容都是字串

r=input("請輸入圓的半徑:")  # 請使用者輸入圓的半徑
r=float(r)  # 將輸入的半徑轉換為浮點數
area=3.14*r**2
print(area)