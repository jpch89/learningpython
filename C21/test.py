'求平方根'
from math import sqrt

li = [2, 4, 9, 16, 25]

# for 循环版本
res = []
for i in li:
    res.append(sqrt(i))
print(res)

# map 版本
print(list(map(sqrt, li)))

# 列表推导式版本
print([sqrt(i) for i in li])

# 生成器版本
print(list(sqrt(i) for i in li))
