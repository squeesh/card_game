import platform

from base.controller import Controller

from gin.deck import GinDeck
from gin.board import GinBoard

class GinController(Controller):
    # if platform.system() == 'Windows':
    #     HEART   = chr(3)
    #     DIAMOND = chr(4)
    #     CLUB    = chr(5)
    #     SPADE   = chr(6)
    # else:
    #     HEART   = '♥'
    #     DIAMOND = '♦'
    #     CLUB    = '♣'
    #     SPADE   = '♠'

    HEART   = 'hearts'
    DIAMOND = 'diamonds'
    CLUB    = 'clubs'
    SPADE   = 'spades'

    SUITS = (HEART, DIAMOND, CLUB, SPADE)

    def get_new_players(self, deck):
        raise NotImplementedError

    def create_game(self):
        deck = GinDeck()
        deck.shuffle_well()

        self.players = self.get_new_players(deck)
        self.active_player = 0

        self.board = GinBoard(self.players, deck)

    def get_deck(self):
        return self.board.deck

    def get_pile(self):
        return self.board.pile
