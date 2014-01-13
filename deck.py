from abc import ABCMeta
from random import random

from util import bridge_shuffle, cut_deck

shuffle_methods = {
    'bridge': bridge_shuffle,
}

class Deck(object, metaclass=ABCMeta):
    cards = None

    def __init__(self, cards=None):
        if cards:
            self.cards = cards
        else:
            self.cards = []

    def __str__(self):
        return 'Deck:\n\t{}'.format('\n\t'.join([str(card) for card in self.cards]))

    def __len__(self):
        return len(self.cards)

    def shuffle_well(self):
        shuffle_deck = int(5 + (random() * 3))
        cut_deck = int(5 + (random() * 5))

        # Thorough shuffle
        for i in range(shuffle_deck):
            self.shuffle()
            for j in range(cut_deck):
                pivot = 0.2 + (random() * 0.6)
                self.cut(pivot=pivot)

    def shuffle(self, method='bridge', pivot=0.5):
        self.cards = shuffle_methods[method](self.cards, pivot=pivot)

    def cut(self, pivot=0.5):
        self.cards = cut_deck(self.cards, pivot=pivot)

    def draw(self, cards_num=1):
        drawn_cards = self.cards[:cards_num]
        self.cards = self.cards[cards_num:]
        return drawn_cards

    def add(self, card, to_top=False):
        if to_top:
            self.cards.insert(0, card)
        else:
            self.cards.append(card)
