from player import Player

from gin.hand import GinHand
from gin.multiplayer.player_input import RemoteConsoleGinPlayerInput


class WebGinPlayer(Player):
    HandClass = GinHand
    InputClass = RemoteConsoleGinPlayerInput
