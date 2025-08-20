# 以下示範 list 的不同型態與內容
print([])  # 空的 list
print([1, 2, 3])  # 含三個整數元素的 list
print([1, 2, 3, "a", "b", "c"])  # 混合型態（整數與字串）的 list，總共 6 個元素
print([1, 2, 3, ["a", "b", "c"]])  # 巢狀 list（最後一個元素是另一個 list）
print([1, True, "a", 1.23])  # 混合整數、布林、字串與浮點數的 list
# CRUD是一個常見的資料操作模式，代表四種基本操作:
#  Create (建立) - 新增元素
#  Read (讀取) - 讀取元素
#  Update (更新) - 更新元素
#  Delete (刪除) - 刪除元素

# CRUD: Read 操作（讀取）
# list 的 index 從 0 開始
L = [1, 2, 3, "a", "b", "c"]
print(L[0])  # 讀取 index 0 的元素 -> 1
print(L[1])  # 讀取 index 1 的元素 -> 2
print(L[2])  # 讀取 index 2 的元素 -> 3
print(L[3])  # 讀取 index 3 的元素 -> "a"

L = [1, 2, 3, "a", "b", "c"]
# 切片語法: L[start:stop:step]
# L[::2] 代表從頭到尾,每隔 2 個元素取一次 -> [1, 3, 'b']
print(L[::2])
# L[1:4] 代表從 index 1 到 index 3 (不包含 4) -> [2, 3, 'a']
print(L[1:4])
# L[1:4:2] 代表從 index 1 到 index 3,每 2 個取一次 -> [2, 'a']
print(L[1:4:2])
# 切片語法與 range 類似，但使用不同符號與語意

# 走訪 list 的兩種常見方法
# 1) 透過 index (需要知道位置或需要跳步長)
# 2) 直接迭代元素 (簡潔且常用)
L = [1, 2, 3, "a", "b", "c"]
for i in range(0, len(L), 2):
    # 使用 index 走訪，每次跳 2 個元素
    print(L[i])

for item in L:
    # 直接把 list 當作可迭代物件，取得每個元素
    print(item)

# CRUD: Update 操作（更新）
# 直接透過 index 指定要修改的位置
L = [1, 2, 3, "a", "b", "c"]
L[0] = 2  # 將 index 0 的元素由 1 改為 2
print(L)

# 範例: 資料複製 vs 參考
# 整數為不可變 (immutable)，賦值會複製值
a = 1
b = a  # b 取得 a 的值（兩者獨立）
b = 2
print(a, b)  # a 不受 b 變動影響 -> (1, 2)

# list 是可變 (mutable)，賦值會建立參考（reference）
a = [1, 2, 3]
b = a  # a 與 b 指向同一個物件
b[0] = 2
print(a, b)  # a 與 b 都會反映改變 -> ([2, 2, 3], [2, 2, 3])

# 若要建立完全獨立的複本，使用 copy()
a = [1, 2, 3]
b = a.copy()  # 建立淺複本，a 與 b 指向不同物件
b[0] = 2
print(a, b)  # 只有 b 改變 -> ([1, 2, 3], [2, 2, 3])

# CRUD: Update 操作（更新）
# list append
L = [1, 2, 3]
L.append(4)  # 在最後面加一個元素
print(L)

# CRUD: Delete 操作（刪除）
# 移除元素有多種方式
# 1) remove(value) 會移除第一個匹配到的值
L = ["a", "b", "c", "d", "a"]
L.remove("a")  # 移除第一個出現的 "a"
# 注意: remove 只會移除第一個匹配項
# 若要移除所有匹配的元素，建議使用 list comprehension 或建立新的 list
L = [x for x in L if x != "a"]  # 建立一個不包含 'a' 的新 list

# 2) pop(index) 依據位置移除元素，若不傳 index 則移除最後一個
L = ["a", "b", "c", "d", "a"]
L.pop(0)  # 移除 index 0 的元素
L.pop()  # 移除最後一個元素
print(L)

# open() 開啟模式
# r -讀取模式,檔案必須存在
# w -寫入模式,檔案不存在會自動建立
# a -附加模式,檔案不存在會自動建立
# r+ -讀取與寫入模式,檔案必須存在
# w+ -讀取與寫入模式,檔案不存在會自動建立
# a+ -讀取與附加模式,檔案不存在會自動建立

# 範例: 使用 open() 讀取檔案內容
f = open("pages/class1-1.py", "r", encoding="utf-8")
content = f.read()  # 讀取整個檔案到字串
print(content)
f.close()  # 使用 open() 時記得關閉檔案

# 建議使用 with 來管理檔案，會自動關閉檔案
with open("pages/class1-1.py", "r", encoding="utf-8") as f:
    content = f.read()
    print(content)

# 字串方法範例: 檔名是否以特定副檔名結尾
filename = "class1.md"
print(filename.endswith(".md"))  # True
filename2 = "notes.txt"
print(filename2.endswith(".md"))  # False
