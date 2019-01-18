class B:
    def __init__(self):
        print('B.__init__')
        print(f'self是{self}')
        super().__init__()

class C:
    def __init__(self):
        print('C.__init__')
        print(f'self是{self}')
        super().__init__()

class D(B, C):
    pass


x = D()
"""
B.__init__
self是<__main__.D object at 0x000001D35CFAC6A0>
C.__init__
self是<__main__.D object at 0x000001D35CFAC6A0>
"""
