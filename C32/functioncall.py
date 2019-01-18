class Test:
    def normal_function():
        print('我是普通函数！')

    @staticmethod
    def static_method():
        print('我是静态方法！')

    @classmethod
    def class_method(cls):
        print(f'我是{cls}的类方法！')

    def instance_method(self):
        print(f'我是{self}的实例方法！')


t = Test()

# 普通函数：只能通过类名调用，不用手动传参
# t.normal_function()
"""
Traceback (most recent call last):
  File "test.py", line 19, in <module>
    t.normal_function()
TypeError: normal_function() takes 0 positional arguments but 1 was given
"""
Test.normal_function()
"""
我是普通函数！
"""

# 静态方法：可以通过实例和类名调用，不用手动传参
t.static_method()
Test.static_method()
"""
我是静态方法！
我是静态方法！
"""

# 类方法：可以通过实例和类名调用，自动传递类给 cls 形参
# 注意：即使通过实例调用类方法，Python 自动传递的也是类，而不是实例
t.class_method()
Test.class_method()
"""
我是<class '__main__.Test'>的类方法！
我是<class '__main__.Test'>的类方法！
"""

# 实例方法：
# 通过实例调用，自动传递实例给 self 形参
# 通过类调用，需要手动传递一个实例给 self 形参
t.instance_method()
Test.instance_method(t)
"""
我是<__main__.Test object at 0x00000189E6A3AC88>的实例方法！
我是<__main__.Test object at 0x00000189E6A3AC88>的实例方法！
"""
# 通过类调用，如果不手动传递实例给 self 形参，会缺少参数的错误
# Test.instance_method()
"""
Traceback (most recent call last):
  File "test.py", line 59, in <module>
    Test.instance_method()
TypeError: instance_method() missing 1 required positional argument: 'self'
"""
