class A:
    def __init__(self):
        print(f'{self}的初始化函数')

class B(A):
    pass

b = B()
print()
"""
<__main__.B object at 0x0000022A185CC1D0>的初始化函数
"""

a = A()
"""
<__main__.A object at 0x0000022A185CC588>的初始化函数
"""
