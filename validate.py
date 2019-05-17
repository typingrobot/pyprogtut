# validate.py


class Integer():
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, cls):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise TypeError('Expected int')
        instance.__dict__[self.name] = value


class Float():
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, cls):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, float):
            raise TypeError('Expected float')
        instance.__dict__[self.name] = value


class Holding():
    shares = Integer('shares')
    price = Float('price')

    def __init__(self, name, date, shares, price):
        self.name = name
        self.date = date
        self.shares = shares
        self.price = price

    @property
    def cost(self):
        return self.shares * self.price


class Point(object):
    x = Integer('x')
    y = Integer('y')

    def __init__(self, x, y):
        self.x = x
        self.y = y
