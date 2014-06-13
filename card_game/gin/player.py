from base.player import Player
from base.controller import Controller

from gin.hand import GinHand
from gin.console.player_input import ConsoleGinPlayerInput


class GinPlayer(Player):
    HandClass = GinHand
    InputClass = ConsoleGinPlayerInput

    def draw_deck(self):
        ctrl = Controller.get()
        return self.draw(ctrl.get_deck())

    def draw_pile(self):
        ctrl = Controller.get()
        return self.draw(ctrl.get_pile())
