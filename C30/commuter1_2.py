class Commuter1:
    def __init__(self, val):
        self.val = val

    def __add__(self, other):
        print('add', self.val, other)
        return self.val + other

    def __radd__(self, other):
        print('radd', self.val, other)
        # return other + self.val
        return self.val + other


x = Commuter1(88)
y = Commuter1(99)

print(x + 1)
print()
"""
add 88 1
89
"""

print(1 + y)
print()
"""
radd 99 1
100
"""

print(x + y)
print()
"""
add 88 <__main__.Commuter1 object at 0x000001CFDDE9C4E0>
radd 99 88
187
"""
# 这里与原来结果一样
# 因为 x + y 首先看 x 的 __add__ 能否处理
# 能处理，输出 add
# 变成 88 + y
# 然后 88 的 __add__ 无法处理，所以看 y 的 __radd__ 能否处理
# 能处理，输出 radd
# 变成 99 + 88
# 输出 187
