class Person:
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay

    def lastName(self):
        return self.name.split()[-1]

    def giveRaise(self, percent):
        self.pay = int(self.pay * (1 + percent))

    def __repr__(self):
        return '[Person: %s, %s]' % (self.name, self.pay)

class Manager(Person):
    def __init__(self, name, pay):
        self.person = Person(name, 'mgr', pay)

    def giveRaise(self, percent, bonus=.10):
        self.person.giveRaise(percent + bonus)

    # def __getattr__(self, attr):
        # return getattr(self.person, attr)

    def __getattribute__(self, attr):
        print('**', attr)
        if attr in ['person', 'giveRaise']:
            return object.__getattribute__(self, attr)
        else:
            return getattr(self.person, attr)

    # def __repr__(self):
        # return str(self.person)

if __name__ == '__main__':
    sue = Person('Sue Jones', job='dev', pay=100000)
    print(sue.lastName())
    sue.giveRaise(.10)
    print(sue)
    tom = Manager('Tom Jones', 50000)
    print(tom.lastName())
    tom.giveRaise(.10)
    print(tom)

