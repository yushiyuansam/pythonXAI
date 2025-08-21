# 字典
# dict是透過key-value的方式來儲存資料,key必須是唯一的,value可以重複
# dict是無序的,所以無法透過index來取得資料
# dict的key必須是不可改變的資料型態,例如int,float,string
# dict的key-value是透過冒號來連接,key:value
# dict的key-value是透過分號來分隔
d = {"a": 1, "b": 2, "c": 3}

# CRUD_read讀取資料
print(d["a"])  # 1
print(d["b"])  # 2
print(d["c"])  # 3

# 取得dict的所有key
print(d.keys())  # ['a', 'b', 'c']
for key in d.keys():
    print(key)

# 取得dict的所有value
print(d.values())  # dict_values([1, 2, 3])
for value in d.values():
    print(value)

# 取得dict的所有key-value
print(d.items())  # [('a', 1), ('b', 2), ('c', 3)]
for key, value in d.items():
    print(key, value)

# CRUD_Create新增/修改資料
# 新增/修改dict的key-value
d["d"] = 4  # 新增
print(d)  # {'a': 1, 'b': 2, 'c': 3, 'd': 4}
# CRUD_Update更新資料
d["a"] = 5  # 修改
print(d)  # {'a': 5, 'b': 2, 'c': 3, 'd': 4}

# CRUD_Delete刪除資料
# 刪除dict的key-value,pop()方法
# 如果資料存在,就刪除並回傳value
print(d.pop("a"))  # 5
# 如果資料不存在,就回傳預設值
print(d.pop("e", "Not Found"))  # Not Found
# 如果資料沒有預設值,就會報錯

# dict的長度
print(len(d))  # 3

# 檢查dict是否存在某個key
# in不能比較value
# 跟list比較,in可以檢查的是list的原素與dict的key
print("a" in d)  # True
print("e" in d)  # False
