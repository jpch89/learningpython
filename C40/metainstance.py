class MetaOne(type):
    def __new__(meta, classname, supers, classdict):
        print('In MetaOne.new:', classname)
        return type.__new__(meta, classname, supers, classdict)

    def toast(self):
        return 'toast'


class Super(metaclass=MetaOne):
    def spam(self):
        return 'spam'


class Sub(Super):
    def eggs(self):
        return 'eggs'


if __name__ == '__main__':
    X = Sub()
    print()
    """
    In MetaOne.new: Super
    In MetaOne.new: Sub
    """

    print(Sub.toast)
    print(Sub.spam)
    # 这里书上写的是 Sub.spam，应该是版本更新有改动
    # spam 方法的前缀现在是定义它的类！
    print(X.spam)
    """
    <bound method MetaOne.toast of <class '__main__.Sub'>>
    <function Super.spam at 0x0000021CD06861E0>
    <bound method Super.spam of <__main__.Sub object at 0x0000021CD068AD68>>
    """
