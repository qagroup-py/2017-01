from collections import defaultdict
from hashlib import sha1


class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __eq__(self, other):
        return self.name == other.name and self.price == other.price

    def __hash__(self):
        return hash((self.name, self.price))


class Cart(defaultdict):
    def __init__(self, *args):
        super().__init__(int, *args)

    @property
    def total(self):
        return sum(item.price * qt for item, qt in self.items())


class User:
    def __init__(self, login, password):
        self.login = login
        self.password = password
        self.cart = Cart()

    def buy(self, item, qt=1):
        self.cart[item] += qt

    @property
    def password(self):
        raise Exception('We do not store password')

    @password.setter
    def password(self, value):
        if len(value) < 6:
            raise Exception('Password too short')
        self.password_hash = sha1(value.encode()).hexdigest()


class Store:
    ...
