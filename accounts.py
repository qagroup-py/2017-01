class InsufficientFundsError(Exception):
    pass


class NegativeAmountError(ValueError):
    pass


class Account:
    def __init__(self, balance, overdraft=0):
        self.balance = balance
        self.overdraft = overdraft

    def __repr__(self):
        """
        Method that gives representation of object in
        interactive python shell
        """
        return 'Account(balance={}, overdraft={})'.format(self.balance, self.overdraft)

    def __str__(self):
        """
        Method used in any str-type casting of object
        '{}'.format(obj) == str(obj) == obj.__str__()
        """
        return 'Account with {} balance'.format(self.balance)

    def transfer(self, other, amount):
        if not isinstance(other, Account):
            raise TypeError
        if amount < 0:
            raise NegativeAmountError()

        if self.balance + self.overdraft >= amount:
            self.balance -= amount
            other.balance += amount
        else:
            raise InsufficientFundsError()


if __name__ == '__main__':
    acc1 = Account(100)
    acc2 = Account(200)
    acc1.transfer(acc2, 50)
    assert acc1.balance == 50
    assert acc2.balance == 250

    acc1 = Account(balance=100, overdraft=50)
    acc2 = Account(200)
    acc1.transfer(acc2, 150)
    assert acc1.balance == -50
    assert acc2.balance == 350

    acc1 = Account(balance=100, overdraft=50)
    acc2 = Account(200)
    try:
        acc1.transfer(acc2, 200)
    except InsufficientFundsError:
        pass
    else:
        raise AssertionError

    acc1 = Account(balance=100)
    acc2 = Account(200)
    try:
        acc1.transfer(acc2, -200)
    except NegativeAmountError:
        pass
    else:
        raise AssertionError
