# for 迴圈搭配 in 使用，in 後面接可疊代的物件 (iterable)
# 最常見的是搭配 range() 產生數值序列
# range(stop): 會產生從 0 到 stop-1 的整數序列（不包含 stop）
for i in range(5):
    print(i)  # 輸出 0,1,2,3,4

# range(start, stop): 從 start 開始，產生到 stop-1 的整數序列
# 例如 range(1,5) 會產生 1,2,3,4（不包含 5）
for i in range(1, 5):
    print(i)  # 輸出 1,2,3,4

# range可以設定起始值和結數值與間格數,但不包含結束值
# range(1,10,2)會產生1,3,5,7,9:
for i in range(1, 10, 2):
    print(i)
