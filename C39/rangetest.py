"""
File rangetest.py: function decorator that performs range-test
validation for arguments passed to any function or method.
Arguments are specified by keyword to the decorator. In the actual
call, arguments may be passed by position or keyword, and defaults
may be omitted. See rangetest_test.py for example use cases.
"""
trace = True

# 调用装饰器的时候，只接收关键字参数
def rangetest(**argchecks):
    def onDecorator(func):
        if not __debug__:
            return func
        # 其实这个 else 可以省略，然后减少缩进层级
        else:
            code = func.__code__
            # co_varnames 元组里面是函数所有局部变量的名称
            # 不包括 *args，强制关键字参数和 **kwargs
            # 被装饰函数和类没有定义 *args、强制关键字参数以及 **kwargs
            # 所以这里取到的就是所有局部变量的名称
            # 存放顺序首先是可调用对象的参数，然后是其他的局部变量
            # co_argcount 属性是参数个数
            # 所以这么取出来的 allargs 就是所有参数
            allargs = code.co_varnames[:code.co_argcount]
            funcname = func.__name__

            def onCall(*pargs, **kargs):
                expected = list(allargs)  # 把切片出来的元组转成列表
                # 用 pargs 的长度切片，剔除默认参数和关键字参数
                # 得到所有位置参数
                positionals = expected[:len(pargs)]

                # **argchecks，其中 argchecks 是一个字典
                # items 得到 (key, value) 这样的一个键值对
                for (argname, (low, high)) in argchecks.items():
                    # 先看这个参数名是不是以关键字形式指定的
                    if argname in kargs:
                        if kargs[argname] < low or kargs[argname] > high:
                            errmsg = '{0} argument "{1}" not in {2}..{3}'
                            errmsg = errmsg.format(funcname, argname, low, high)
                            raise TypeError(errmsg)

                    # 如果不是以关键字形式指定的
                    elif argname in positionals:
                        position = positionals.index(argname)
                        if pargs[position] < low or pargs[position] > high:
                            # 这里其实可以提取冗余代码封装成函数
                            errmsg = '{0} argument "{1}" not in {2}..{3}'
                            errmsg = errmsg.format(funcname, argname, low, high)
                            raise TypeError(errmsg)
                    else:
                        if trace:
                            print('Argument "{0}" defaulted'.format(argname))
                # onCall 就是装饰器运行后实际被调用的东西
                # 首先进行了参数检查
                # 检查没问题之后返回原来函数调用
                return func(*pargs, **kargs)
            # 这里要返回包装器 Wrapper
            # 也就是最终函数会变成这个
            return onCall
    # 最外层返回一个装饰器
    return onDecorator
