import random


class Deck:
    def __init__(self):
        self.create_deck()

    def create_deck(self):
        suits = ['heart', 'diamond', 'spade', 'club']
        ranks = list(range(2,11)) + ['J', 'Q', 'K', 'A']
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append((suit, rank))

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        return self.deck.pop(0)