from player import Player
from gin.hand import GinHand
from gin.player_input import ConsoleGinPlayerInput, RemoteConsoleGinPlayerInput


class GinPlayer(Player):
    HandClass = GinHand
    InputClass = ConsoleGinPlayerInput


class RemoteGinPlayer(Player):
    HandClass = GinHand
    InputClass = RemoteConsoleGinPlayerInput
