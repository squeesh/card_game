from base.player import Player

from gin.hand import GinHand
from gin.console.player_input import ConsoleGinPlayerInput


class GinPlayer(Player):
    HandClass = GinHand
    InputClass = ConsoleGinPlayerInput
