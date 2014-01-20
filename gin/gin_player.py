from player import Player, RemotePlayer
from gin.gin_hand import GinHand
from gin.gin_player_input import ConsoleGinPlayerInput


class GinPlayer(Player):
    HandClass = GinHand
    InputClass = ConsoleGinPlayerInput


class RemoteGinPlayer(RemotePlayer):
    HandClass = GinHand
