from player import Player, RemotePlayer
from gin.gin_hand import GinHand


class GinPlayer(Player):
    HandClass = GinHand


class RemoteGinPlayer(RemotePlayer):
    HandClass = GinHand
