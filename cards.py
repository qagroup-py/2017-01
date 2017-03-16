from random import shuffle, randint


# followint class can be written as
# from collections import namedtuple
# Card = namedtuple('Card', 'rank, suit')
class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __repr__(self):
        return "Card(rank='{}', suit='{}')".format(self.rank, self.suit)

    def __eq__(self, other):
        return self.rank == other.rank and self.suit == other.suit

    def __hash__(self):
        return hash(self.rank, self.suit)


class Deck:
    suits = ['spades', 'clubs', 'hearts', 'diamonds']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

    def __init__(self):
        self.cards = []
        for suit in self.suits:
            for rank in self.ranks:
                self.cards.append(Card(rank, suit))

    def draw(self):
        return self.cards.pop()

    def shuffle(self):
        shuffle(self.cards)

    def add(self, card):
        self.cards.append(card)

    def insert(self, card, position=None):
        if position is None:
            position = randint(0, len(self.cards))
        self.cards.insert(position, card)

    def count(self):
        return len(self.cards)
