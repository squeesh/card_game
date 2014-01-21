from player import Player
from gin.gin_hand import GinHand
from gin.gin_player_input import ConsoleGinPlayerInput, RemoteConsoleGinPlayerInput


class GinPlayer(Player):
    HandClass = GinHand
    InputClass = ConsoleGinPlayerInput


class RemoteGinPlayer(Player):
    HandClass = GinHand
    InputClass = RemoteConsoleGinPlayerInput
