from player import Player
from gin.hand import GinHand
from gin.player_input import ConsoleGinPlayerInput


class GinPlayer(Player):
    HandClass = GinHand
    InputClass = ConsoleGinPlayerInput
