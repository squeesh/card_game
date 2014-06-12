from gin.controller import GinController
from gin.multiplayer.player import RemoteGinPlayer
from gin.player import GinPlayer


class LocalRemoteGinController(GinController):
    def get_players(self, deck):
        return (GinPlayer(deck.draw_many(11), 1), RemoteGinPlayer(deck.draw_many(11), 2))
