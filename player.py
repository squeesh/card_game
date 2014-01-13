
from hand import Hand

class Player(object):
    hand = None
    HandClass = Hand

    def __init__(self, cards):
        self.hand = self.HandClass()
        self.hand.add(cards)
