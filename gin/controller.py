import platform

from controller import Controller

from gin.deck import GinDeck
from gin.player import GinPlayer
from gin.board import GinBoard

class GinController(Controller):
    if platform.system() == 'Windows':
        HEART   = chr(3)
        DIAMOND = chr(4)
        CLUB    = chr(5)
        SPADE   = chr(6)
    else:
        HEART   = '♥'
        DIAMOND = '♦'
        CLUB    = '♣'
        SPADE   = '♠'

    SUITS = (HEART, DIAMOND, CLUB, SPADE)

    def get_players(self, deck):
        raise NotImplementedError

    def create_game(self):
        deck = GinDeck()
        deck.shuffle_well()

        self.players = self.get_players(deck)
        self.active_player = 0

        self.board = GinBoard(self.players, deck)


class AllLocalGinController(GinController):
    def get_players(self, deck):
        return (GinPlayer(deck.draw(11), 1), GinPlayer(deck.draw(11), 2))
