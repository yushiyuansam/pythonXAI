a = 1
a += 1
print(a)
a -= 1
print(a)
a *= 2
print(a)
a /= 2
print(a)
a //= 2
print(a)
a %= 2
print(a)
a **= 2
print(a)

# 優先順序
# 1.括號
# 2.次方
# 3.乘除
# 4.加減
# 5.比較運算== != > < >= <=
# 6.not
# 7.and
# 8.or
# 9.= += -= *= /= % //= %= **= 算數指定運算子
# while會搭配一個條件式來使用
# 條件式為True時會一直執行迴圈
# 條件式為false時會跳出迴圈
# 每次迴圈執行完都會重新檢查條件有沒有變成False
i = 0
while i < 5:
    print(i)
    i += 1
# break 可以強制
# 先判斷break屬於哪個迴圈,然後跳出該迴圈
i = 0
while i < 5:
    print(i)

    for j in range(5):
        print(j)

    if i == 3:
        break  # 跳出迴圈,屬於while迴圈
    i += 1

    for i in range(5):
        print(i)
        if i == 3:
            break  # 跳出迴圈

    import random  # 匯入randoma模組

    # random.randrange()設定了抽籤範圍的方式跟range()一樣
    print(random.randrange(7))  # 0~6
    print(random.randrange(1, 6))  # 1~6
    print(random.randrange(1, 6, 2))  # 1~6,2的倍數

    # random.randint()設定了抽籤範圍的方式一定要設定開始與結束
    # 且結的數字會包含在內
    print(random.randint(1, 6))  # 1~6
