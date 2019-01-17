'Commuter1 的变体'

class Commuter1:
    def __init__(self, val):
        self.val = val

    def __add__(self, other):
        print('add', self.val, other)
        # return self.val + other
        return other + self.val

    def __radd__(self, other):
        print('radd', self.val, other)
        return other + self.val


x = Commuter1(88)
y = Commuter1(99)

print(x + 1)
print()
"""
add 88 1
89
"""

print(1 + y)  # 这里调用 1 的 __add__ 行不通，所以调用 y 的 __radd__
print()
"""
radd 99 1
100
"""

print(x + y)
print()
# 首先调用 x 的 __add__
# 变成 y + 88
# 然后调用 y 的 __add__
# 变成 88 + 99
# 所以出现了两次 add
"""
add 88 <__main__.Commuter1 object at 0x0000021A64DFC4E0>
add 99 88
187
"""

