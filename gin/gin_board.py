
from board import Board

class GinBoard(Board):
    deck = None

    def __init__(self, players, deck):
        self.deck = deck
        super(GinBoard, self).__init__(players=players)
