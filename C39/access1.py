"""
File access1.py (3.X + 2.X)
Privacy for attributes fetched from class instances.
See self-test code at end of file for a usage example.
Decorator same as: Doubler = Private('data', 'size')(Doubler).
Private returns onDecorator, onDecorator returns onInstance,
and each onInstance instance embeds a Doubler instance.
"""

traceMe = False


def trace(*args):
    if traceMe:
        print('[' + ' '.join(map(str, args)) + ']')


# Private 实际上是个带参装饰器，所以有三层
# 1. Private 函数，返回一个装饰器
# 2. onDecorator 函数，返回一个类
# 3. onInstance 类，被装饰的类实例化的时候实际上运行的就是它
# privates 是一个元组，里面放着所有私有属性
def Private(*privates):         # privates in enclosing scope
    def onDecorator(aClass):    # aClass in enclosing scope
        class onInstance:       # wrapped in instance attribute
            def __init__(self, *args, **kargs):
                # 把 Doubler 类的实例包装在 onInstance 实例属性 wrapped 上
                self.wrapped = aClass(*args, **kargs)

            # 这里会拦截类外面取属性的操作
            # 比如 label，data
            def __getattr__(self, attr):   # My attrs don't call getattr
                trace('get:', attr)        # Others assumed in wrapped
                if attr in privates:  # 如果该属性在私有属性元组中
                    # 抛出异常
                    raise TypeError('private attribute fetch: ' + attr)
                else:  # 如果该属性没有在私有属性元组，直接从被包装的对象中取属性
                    return getattr(self.wrapped, attr)

            # 这里会拦截类外面设置属性的操作
            def __setattr__(self, attr, value):   # Outside accesses
                trace('set:', attr, value)        # Others run normally
                # 如果设置的是 wrapped
                # 说明是初始化的时候，onInstance 实例需要设置这个属性
                # 那么不要拦截，通过属性字典设置
                if attr == 'wrapped':             # Allow my attrs
                    self.__dict__[attr] = value   # Avoid looping
                # 如果设置的属性在私有属性元组中
                elif attr in privates:
                    # 抛出异常
                    raise TypeError('private attribute change: ' + attr)
                else:
                    # 否则的话，不是私有属性，把设置操作路由（分发）给 self.wrapped
                    # 即 Doubler 实例
                    setattr(self.wrapped, attr, value)  # Wrapped obj attrs
        return onInstance  # Or use __dict__
    return onDecorator


if __name__ == '__main__':
    traceMe = True

    # 这里设置了两个私有属性，data 和 size
    @Private('data', 'size')     # Doubler = Private(...)(Doubler)
    class Doubler:
        # 类内部的属性操作不会被拦截
        # 因为类内部的 self 就是 Doubler 实例，而不是 onInstance 实例
        # Doubler 所有属性的赋值与取值都是开放的
        def __init__(self, label, start):
            self.label = label   # Accesses inside the subject class
            self.data = start    # Not intercepted: run normally

        def size(self):
            return len(self.data)  # Methods run with no checking

        def double(self):          # Because privacy not inherited
            for i in range(self.size()):
                self.data[i] = self.data[i] * 2

        def display(self):
            print('%s => %s' % (self.label, self.data))

    # 实际上是调用了 onInstance 类进行创建
    # 创建过程中调用了 onInstance 类的初始化方法 __init__
    # 设置 self.wrapped 的时候触发了 onInstance 类的 __setattr__ 方法
    X = Doubler('X is', [1, 2, 3])  # label 被设置成 X is，data 被设置成 [1, 2, 3]
    Y = Doubler('Y is', [-10, -20, -30])  # label 被设置成 Y is，data 被设置成 [-10, -20, -30]
    print()
    """
    [set: wrapped <__main__.Doubler object at 0x000001726FA74278>]
    [set: wrapped <__main__.Doubler object at 0x000001726FA742E8>]
    """

    # The following all succeed
    # 外部访问，触发 onInstance 的 __getattr__
    # 不是私有属性，正常输出
    print(X.label)  # Accesses outside subject class
    print()
    """
    [get: label]
    X is
    """

    X.display(); X.double(); X.display()  # Intercepted: validated, delegated
    print()
    """
    [get: label]
    X is
    [get: display]
    X is => [1, 2, 3]
    [get: double]
    [get: display]
    X is => [2, 4, 6]
    """

    print(Y.label)
    print()
    """
    [get: label]
    Y is
    """

    Y.display()
    Y.double()
    Y.label = 'Spam'
    Y.display()
    """
    [get: display]
    Y is => [-10, -20, -30]
    [get: double]
    [set: label Spam]
    [get: display]
    Spam => [-20, -40, -60]
    """

    # The following all fail properly
    """
    print(X.size())  # prints "TypeError: private attribute fetch: size"
    print(X.data)
    X.data = [1, 1, 1]
    X.size = lambda S: 0
    print(Y.data)
    print(Y.size())
    """
