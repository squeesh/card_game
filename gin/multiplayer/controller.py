from gin.player import GinPlayer
from gin.multiplayer.player import RemoteGinPlayer

from gin.controller import GinController

class LocalRemoteGinController(GinController):
    def get_players(self, deck):
        return (GinPlayer(deck.draw(11), 1), RemoteGinPlayer(deck.draw(11), 2))
