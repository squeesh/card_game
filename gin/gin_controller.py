import platform
import re

from controller import Controller

from gin.gin_deck import GinDeck
from gin.gin_hand import GinHand
from gin.gin_player import GinPlayer
from gin.gin_board import GinBoard

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

    def create_game(self):
        deck = GinDeck()
        deck.shuffle_well()

        players = (
            GinPlayer(deck.draw(11)),
            GinPlayer(deck.draw(11)),
        )

        self.board = GinBoard(players, deck)

    def main_loop(self):
        print('Welcome to shitty Gin', ' '.join(GinController.SUITS))

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
5 X Y| Move card X to new position Y in your hand
6 X  | Discard X card from hand
end  | End turn

exit | Exit game
""".format(player_index + 1)
            )

            data = input('Command: ')

            if re.match('^1$', data):
                print(curr_player.hand)

            elif re.match('^2$', data):
                if self.board.pile.cards:
                    print(self.board.pile.cards[0])
                else:
                    print('Pile is empty')

            elif re.match('^3$', data):
                drawn = self.board.deck.draw()
                curr_player.hand.add(drawn)
                print('You drew: ', drawn)

            elif re.match('^4$', data):
                if self.board.pile.cards:
                    drawn = self.board.pile.draw()
                    curr_player.hand.add(drawn)
                    print('You drew: ', drawn)
                else:
                    print('Error: Pile empty')

            elif re.match('^5 \d+ \d+$', data):
                _, pos_a, pos_b = data.split(' ')
                pos_a, pos_b = int(pos_a), int(pos_b)
                curr_player.hand.move(pos_a, pos_b)
                print(curr_player.hand)

            elif re.match('^6 \d+$', data):
                _, pos = data.split(' ')
                print('You discarded: ', curr_player.discard(int(pos)))
                print(curr_player.hand)

            elif re.match('^end$', data):
                player_index = 0 if player_index else 1
                curr_player = self.board.players[player_index]

            elif re.match('^exit$', data):
                break
            else:
                print('Error: Please rekey')



