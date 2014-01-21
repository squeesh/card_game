import platform

from controller import Controller
import settings

from gin.gin_deck import GinDeck
from gin.gin_hand import GinHand
from gin.gin_player import GinPlayer, RemoteGinPlayer
from gin.gin_board import GinBoard

class BaseGinController(Controller):
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


class GinController(BaseGinController):
    def create_game(self):
        deck = GinDeck()
        deck.shuffle_well()

        self.players = (
            GinPlayer(deck.draw(11), 1),
            RemoteGinPlayer(deck.draw(11), 2),
        )
        self.active_player = 0

        self.board = GinBoard(self.players, deck)


# class ServerGinController(BaseGinController):
#     def create_game(self):
#         deck = GinDeck()
#         deck.shuffle_well()

#         self.players = (
#             GinPlayer(deck.draw(11)),
#             RemoteGinPlayer(deck.draw(11)),
#         )

#         self.board = GinBoard(players, deck)

# class ClientGinController(BaseGinController):
#     pass

