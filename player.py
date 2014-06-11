from controller import Controller
from hand import Hand
from player_input import PlayerInput


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

    def discard(self, pos):
        ctrl = Controller.get()

        discard = self.hand.discard(pos)
        ctrl.board.pile.add(discard, to_top=True)

        return discard

    def process_input(self):
        self.input.process()
