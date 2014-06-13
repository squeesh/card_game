from base.controller import Controller
from base.hand import Hand
from base.player_input import PlayerInput


class Player(object):
    HandClass = Hand
    InputClass = PlayerInput

    hand = None
    input = None
    player_num = 0

    def __init__(self, cards, player_num):
        self.hand = self.HandClass()
        self.hand.add(cards)

        self.input = self.InputClass()
        self.input.player = self

        self.player_num = player_num

    def draw(self, deck):
        ctrl = Controller.get()

        drawn = deck.draw()
        self.hand.add(drawn)
        return drawn

    def discard(self, pos):
        raise NotImplementedError

    def process_input(self):
        self.input.process()
