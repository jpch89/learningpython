class Wrapper:
    def __init__(self, obj):
        self.wrapped = obj

    def __getattr__(self, attrname):
        print('Trace: ' + attrname)
        return getattr(self.wrapped, attrname)

x = Wrapper([1, 2, 3])
x.append(4)
print(x.wrapped)
"""
Trace: append
[1, 2, 3, 4]
"""
