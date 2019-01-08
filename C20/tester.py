from scramble import scramble
from inter2 import intersect, union

def tester(func, items, trace=True):
    for args in scramble(items):
        if trace: print(args)
        print(sorted(func(*args)))

tester(intersect, ('aab', 'abcde', 'ababab'))

"""
('aab', 'abcde', 'ababab')
['a', 'b']
('abcde', 'ababab', 'aab')
['a', 'b']
('ababab', 'aab', 'abcde')
['a', 'b']
"""
