from gin.controller import GinController
from gin.player import GinPlayer


class WebGinController(GinController):
    def get_players(self, deck):
        return (GinPlayer(deck.draw_many(11), 1), GinPlayer(deck.draw_many(11), 2))
