from models import User, Item, buy


# user buys item
item = Item(name='banana', price=2)
user = User('user10', 'passwd')
buy(user, item, 5)

assert user.cart[item] == 5
assert user.cart.total == 10
