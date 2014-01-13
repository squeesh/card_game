
from hand import Hand

class Player(object):
    hand = None
    HandClass = Hand

    def __init__(self, cards):
        self.hand = self.HandClass()
        self.hand.add(cards)

    def discard(self, pos):
        from gin.gin_controller import GinController

        ctrl = GinController.get()
        ctrl.board.pile.add(self.hand.discard(pos))
