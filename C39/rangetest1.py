def rangetest(*argchecks):
    def onDecorator(func):
        # 默认为 True
        # python -O main.py args... 才为 False
        if not __debug__:
            return func
        else:
            def onCall(*args):
                # 这里的 ix 指的是 index
                # 即检查第几个参数
                for (ix, low, high) in argchecks:
                    if args[ix] < low or args[ix] > high:
                        errmsg = 'Argument %s not in %s..%s' % (ix, low, high)
                        raise TypeError(errmsg)
                return func(*args)
            return onCall
        return onDecorator
