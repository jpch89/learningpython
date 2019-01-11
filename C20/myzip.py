def myzip(*args):
    iters = list(map(iter, args))
    while iters:
        res = [next(i) for i in iters]
        yield tuple(res)

print(list(myzip()))

"""
[('a', 'l'), ('b', 'm'), ('c', 'n')]
"""
