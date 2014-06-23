from gin.controller import GinController
from gin.player import GinPlayer


class WebGinController(GinController):
    def get_new_players(self, deck):
        return (GinPlayer(deck.draw_many(11), 1), GinPlayer(deck.draw_many(11), 2))

    def get_player_for_user(self, user):
        for player in self.players:
            if user.id == player.user.id:
                return player

    def get_opponent_for_user(self, user):
        for player in self.players:
            if user.id != player.user.id:
                return player
