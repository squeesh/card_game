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

        # print(deck)
        # print(len(deck))

        # print()
        # print('Player 1')
        # print(self.board.players[0].hand)
        # print()
        # print('Player 2')
        # print(self.board.players[1].hand)

        # print()
        # print(self.board.pile)
        # print('Player 1 discard...')
        # self.board.players[0].discard(2)
        # print(self.board.pile)

        # print()
        # print(self.board.players[0].hand)

    def main_loop(self):
        print('Welcome to shitty Gin', ' '.join(chr(n) for n in range(3, 3+4)))

        player_index = 0
        curr_player = self.board.players[player_index]

        while True:
            print(
"""
Player {}
1    | View hand
2    | View top card of pile
3    | Draw card from Deck
4    | Draw top card from pile
5 X  | Discard X card from hand
end  | End turn

exit | Exit game
""".format(player_index + 1)
            )

            data = input('Command: ')

            if data == '1':
                print(curr_player.hand)
            elif data == '2':
                if self.board.pile.cards:
                    print(self.board.pile.cards[0])
                else:
                    print('Pile is empty')

            elif data == '3':
                drawn = self.board.deck.draw()
                curr_player.hand.add(drawn)
                print('You drew: ', drawn)
            elif data == '4':
                if self.board.pile.cards:
                    drawn = self.board.pile.draw()
                    curr_player.hand.add(drawn)
                    print('You drew: ', drawn)
                else:
                    print('Error: Pile empty')
            elif data[0] == '5':
                _, pos = data.split(' ')
                print('You discarded: ', curr_player.discard(int(pos)))
            elif data == 'end':
                player_index = 0 if player_index else 1
                curr_player = self.board.players[player_index]
            elif data == 'exit':
                break
            else:
                print('Error: Please rekey')



