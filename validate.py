# validate.py


class Typed():
    expected_type = object

    def __init__(self, name):
        self.name = name

    def __get__(self, instance, cls):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, self.expected_type):
            raise TypeError('Expected {}'.format(self.expected_type))
        instance.__dict__[self.name] = value


class Integer(Typed):
    expected_type = int


class Float(Typed):
    expected_type = float


class String(Typed):
    expected_type = str


class Holding():
    name = String('name')
    shares = Integer('shares')
    price = Float('price')

    def __init__(self, name, date, shares, price):
        self.name = name
        self.date = date
        self.shares = shares
        self.price = price

    def __setattr__(self, name, value):
        if name not in {'name', 'date', 'shares', 'price'}:
            raise AttributeError('No attribute {}'.format(name))
        super().__setattr__(name, value)

    @property
    def cost(self):
        return self.shares * self.price


class Point(object):
    x = Integer('x')
    y = Integer('y')

    def __init__(self, x, y):
        self.x = x
        self.y = y
