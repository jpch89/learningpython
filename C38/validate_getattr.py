class CardHolder:
    acctlen = 8
    retireage = 59.5

    def __init__(self, acct, name, age, addr):
        self.acct = acct
        self.name = name
        self.age = age
        self.addr = addr

    def __getattr__(self, name):
        if name == 'acct':
            return self._acct[:-3] + '***'
        elif name == 'remain':
            return self.retireage - self.age
        else:
            raise AttributeError(name)

    def __setattr__(self, name, value):
        if name == 'name':
            value = value.lower().replace(' ', '_')
        elif name == 'age':
            if value < 0 or value > 150:
                raise ValueError('invalid age')
        elif name == 'acct':
            name = '_acct'
            value = value.replace('-', '')
            if len(value) != self.acctlen:
                raise TypeError('invalid acct number')
        elif name == 'remain':
            raise TypeError('cannot set remain')
        self.__dict__[name] = value

