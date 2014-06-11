from gin.controller import GinController
from gin.player import GinPlayer


class AllLocalGinController(GinController):
    def get_players(self, deck):
        return (GinPlayer(deck.draw(11), 1), GinPlayer(deck.draw(11), 2))
