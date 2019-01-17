class Commuter1:
    def __init__(self, val):
        self.val = val

    def __add__(self, other):
        print('add', self.val, other)
        return self.val + other

    def __radd__(self, other):
        print('radd', self.val, other)
        return other + self.val


x = Commuter1(88)
y = Commuter1(99)

print(x + 1)
"""
add 88 1
89
"""

print(1 + y)
"""
radd 99 1
100
"""

print(x + y)
"""
add 88 <__main__.Commuter1 object at 0x000002C0C5CAC4E0>
radd 99 88
187
"""
