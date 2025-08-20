import random  # 引入 random 模組，用來產生隨機整數

# 猜數字遊戲：電腦隨機產生一個 1~100 的整數，使用者重複輸入數字來猜，直到猜中為止
ans = random.randint(1, 100)  # 隨機產生答案，範圍包含 1 與 100

# 記錄目前允許輸入的上下界（提示用），初始為 1 ~ 100
max_num = 100
min_num = 1

while True:  # 無限迴圈，直到使用者猜中（使用 break 跳出）
    # input() 會回傳字串，使用 int() 轉成整數；若使用者輸入非整數會產生 ValueError
    # f-string 用來顯示目前的範圍提示
    num = int(input(f"請輸入{min_num}~{max_num}的整數："))

    # 若使用者輸入的數字比答案大
    if num > ans:
        print("太大了")  # 提示太大
        # 若使用者輸入的數字比目前的 max 還小，表示可以把 max 縮小為該輸入值
        # 這樣下一次提示的上界會變小，幫助使用者收斂範圍
        if num < max_num:
            max_num = num

    # 若使用者輸入的數字比答案小
    elif num < ans:
        print("太小了")  # 提示太小
        # 若使用者輸入的數字比目前的 min 還大，表示可以把 min 增大為該輸入值
        # 這樣下一次提示的下界會變大，幫助使用者收斂範圍
        if num > min_num:
            min_num = num

    # 使用者猜中
    else:
        print("答對了")
        break  # 跳出迴圈，遊戲結束
