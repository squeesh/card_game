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


        # self.deck = GinDeck()

        # shuffle_deck = int(5 + (random() * 3))
        # cut_deck = int(5 + (random() * 5))

        # # Thorough shuffle
        # for i in range(shuffle_deck):
        #     self.deck.shuffle()
        #     for j in range(cut_deck):
        #         pivot = 0.2 + (random() * 0.6)
        #         self.deck.cut(pivot=pivot)

        # print(self.deck)

        # hand = GinHand()
        # hand.add(self.deck.draw(7))

        # print()
        # print(hand)
        # print()
        # print(len(self.deck))

