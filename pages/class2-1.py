# 比較運算子示範 (Comparison operators)
# 比較運算會回傳布林值 (True 或 False)，常用於條件判斷
# ==  等於
# !=  不等於
# >   大於
# <   小於
# >=  大於等於
# <=  小於等於


print(1 == 1)  # 等於：1 是否等於 1，結果 True
print(1 != 1)  # 不等於：1 是否不等於 1，結果 False
print(1 > 1)  # 大於：1 是否大於 1，結果 False
print(1 < 1)  # 小於：1 是否小於 1，結果 False
print(1 >= 1)  # 大於等於：1 是否大於或等於 1，結果 True
print(1 <= 1)  # 小於等於：1 是否小於或等於 1，結果 True

# 布林值與邏輯運算 (Boolean values & logical operators)
# and: 只有左右兩邊都為 True 時，結果才是 True
print(True and True)  # True and True -> True
print(True and False)  # True and False -> False
print(False and True)  # False and True -> False
print(False and False)  # False and False -> False

# or: 只要左右任一為 True，結果就是 True
print(True or True)  # True or True -> True
print(True or False)  # True or False -> True
print(False or True)  # False or True -> True
print(False or False)  # False or False -> False

# not: 反轉布林值
print(not True)  # not True -> False
print(not False)  # not False -> True

# 優先順序
# 1.括號
# 2.次方
# 3.乘除
# 4.加減
# 5.比較運算== != > < >= <=
# 6.not
# 7.and
# 8.or

password = input("請輸入密碼：")  # input() 回傳字串，存在變數 password
if password == "1234":
    print("歡迎 Sunny！")  # 當密碼為 1234 時顯示歡迎訊息
elif password == "5678":
    print("歡迎 Jack！")  # 當密碼為 5678 時顯示歡迎訊息
elif password == "0000":
    print("歡迎 Mary！")  # 當密碼為 0000 時顯示歡迎訊息
else:
    print("密碼錯誤，請重新輸入！")
# 連續使用if跟使用if...elif...else的差異
# elif可以排除前面有判斷過的條件,所以縮短判斷複雜度,也解省時間
# 但是如果是使用多個if來做獨立判斷,則每個if都會被執行,所以效率會比較低
