import time

def timer(func, *args):
    start = time.clock()
    for i in range(1000):
        func(*args)
    return time.clock() - start

print(timer(pow, 2, 1000))
"""
0.0010321225267323304
"""

print(timer(str.upper, 'spam'))
"""
9.326139562778083e-05
"""
