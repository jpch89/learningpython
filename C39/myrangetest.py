def rangetest(*, percent):
    def decorator(func):
        def wrapper(self, given_percent):
            if given_percent < percent[0] or given_percent > percent[1]:
                raise ValueError('invalid percentage')
            res = func(self, given_percent)
            return res
        return wrapper
    return decorator


class Person:
    @rangetest(percent=(0.0, 1.0))
    def giveRaise(self, percent):
        self.pay = int(self.pay * (1 + percent))


if __name__ == '__main__':
    p = Person()
    p.pay = 100
    p.giveRaise(1.1)
    print(p.pay)

"""
Traceback (most recent call last):
  File "rangetest.py", line 21, in <module>
    p.giveRaise(1.1)
  File "rangetest.py", line 5, in wrapper
    raise ValueError('invalid percentage')
ValueError: invalid percentage
"""
