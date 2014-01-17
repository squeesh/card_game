
from board import Board

from deck import Deck
from gin.gin_deck import GinDeck

class GinBoard(Board):
    deck = None
    pile = None

    def __init__(self, players, deck):
        self.deck = deck
        self.pile = Deck()

        super(GinBoard, self).__init__(players=players)
