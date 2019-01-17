class Commuter5:  # Propagate class type in results
    def __init__(self, val):
        self.val = val

    def __add__(self, other):
        if isinstance(other, Commuter5):  # Type test to avoid object nesting
            other = other.val
        return Commuter5(self.val + other)  # Else + result is another Commuter

    def __radd__(self, other):
        return Commuter5(other + self.val)

    def __str__(self):
        return '<Commuter5: %s>' % self.val

x = Commuter5(88)
y = Commuter5(99)

print(x + 10)
print()
"""
<Commuter5: 98>
"""

print(10 + y)
print()
"""
<Commuter5: 109>
"""

z = x + y
print(z)
print()
"""
<Commuter5: 187>
"""
# 如果不进行类型判断，会变成
# <Commuter5: <Commuter5: 187>>

print(z + 10)
print()
"""
<Commuter5: 197>
"""
# 如果不进行类型判断，会变成
# <Commuter5: <Commuter5: 197>>
