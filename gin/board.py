from base.board import Board
from base.deck import Deck

from gin.deck import GinDeck


class GinBoard(Board):
    deck = None
    pile = None

    def __init__(self, players, deck):
        self.deck = deck
        self.pile = Deck()

        super(GinBoard, self).__init__(players=players)
