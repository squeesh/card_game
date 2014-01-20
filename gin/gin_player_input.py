import re

from exceptions import InputValidationException
from player_input import PlayerInput



class ConsoleGinPlayerInput(object):
    def process(self):
        from gin.gin_controller import GinController
        ctrl = GinController.get()

        curr_player = self.player

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
""".format(curr_player.player_num)
        )

        data = input('Command: ')

        try:
            if re.match('^1$', data):
                print(curr_player.hand)

            elif re.match('^2$', data):
                if ctrl.board.pile.cards:
                    print(ctrl.board.pile.cards[0])
                else:
                    print('Pile is empty')

            elif re.match('^3$', data):
                drawn = ctrl.board.deck.draw()
                curr_player.hand.add(drawn)
                print('You drew: ', drawn)

            elif re.match('^4$', data):
                if ctrl.board.pile.cards:
                    drawn = ctrl.board.pile.draw()
                    curr_player.hand.add(drawn)
                    print('You drew: ', drawn)
                else:
                    print('Error: Pile empty')

            elif re.match('^5 \d+ \d+$', data):
                _, pos_a, pos_b = data.split(' ')
                pos_a, pos_b = int(pos_a), int(pos_b)

                cards_in_hand = len(curr_player.hand.cards)
                if pos_a < 0 or pos_a >= cards_in_hand or pos_b < 0 or pos_b >= cards_in_hand:
                    raise InputValidationException()

                curr_player.hand.move(pos_a, pos_b)
                print(curr_player.hand)

            elif re.match('^6 \d+$', data):
                _, pos = data.split(' ')
                pos = int(pos)

                cards_in_hand = len(curr_player.hand.cards)
                if pos < 0 or pos >= cards_in_hand:
                    raise InputValidationException()

                print('You discarded: ', curr_player.discard(pos))
                print(curr_player.hand)

            elif re.match('^end$', data):
                ctrl.next_turn()

            elif re.match('^exit$', data):
                ctrl.force_exit = True
            else:
                raise InputValidationException()

        except InputValidationException:
            print()
            print('Error: Please rekey')