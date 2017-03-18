from collections import defaultdict


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
        super().__init__(int)

    @property
    def total(self):
        return sum(item.price * qt for item, qt in self.items())


class User:
    def __init__(self, login, password):
        self.login = login
        self.password = hash(password)
        self.cart = Cart()


class Store:
    ...


def buy(user, item, qt=1):
    user.cart[item] += qt
