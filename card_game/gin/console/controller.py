from gin.controller import GinController
from gin.player import GinPlayer


class AllLocalGinController(GinController):
    def get_new_players(self, deck):
        return (GinPlayer(deck.draw_many(11), 1), GinPlayer(deck.draw_many(11), 2))
