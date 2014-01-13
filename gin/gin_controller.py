from controller import Controller

from gin.gin_deck import GinDeck
from gin.gin_hand import GinHand
from gin.gin_player import GinPlayer
from gin.gin_board import GinBoard

class GinController(Controller):
    def create_game(self):
        deck = GinDeck()
        deck.shuffle_well()

        players = (
            GinPlayer(deck.draw(11)),
            GinPlayer(deck.draw(11)),
        )

        self.board = GinBoard(players, deck)

        print(deck)
        print(len(deck))

        print()
        print('Player 1')
        print(self.board.players[0].hand)
        print()
        print('Player 2')
        print(self.board.players[1].hand)

        print()
        print(self.board.pile)
        print('Player 1 discard...')
        self.board.players[0].discard(2)
        print(self.board.pile)

        print()
        print(self.board.players[0].hand)
