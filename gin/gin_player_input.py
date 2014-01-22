import re
from io import StringIO
import sys
import pickle
import socket

from exceptions import InputValidationException
from player_input import PlayerInput


class ConsoleGinPlayerInput(PlayerInput):
    output_buffer = sys.stdout

    def print_data(self, *args, command=None, **kwargs):
        from gin.gin_controller import GinController
        ctrl = GinController.get()

        if not command:
            command = ctrl.COMMANDS['NO_ACTION']
        print(*args, file=self.output_buffer, **kwargs)

    def get_input(self):
        return input('Command: ')

    def print_menu(self, ctrl):
        self.print_data(
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
""".format(self.player.player_num), command=ctrl.COMMANDS['GET_INPUT']
        )

    def input_action(self, ctrl, data):
        try:
            if re.match('^1$', data):
                self.print_data(self.player.hand)

            elif re.match('^2$', data):
                if ctrl.board.pile.cards:
                    self.print_data(ctrl.board.pile.cards[0])
                else:
                    self.print_data('Pile is empty')

            elif re.match('^3$', data):
                drawn = ctrl.board.deck.draw()
                self.player.hand.add(drawn)
                self.print_data('You drew: ', drawn)

            elif re.match('^4$', data):
                if ctrl.board.pile.cards:
                    drawn = ctrl.board.pile.draw()
                    self.player.hand.add(drawn)
                    self.print_data('You drew: ', drawn)
                else:
                    self.print_data('Error: Pile empty')

            elif re.match('^5 \d+ \d+$', data):
                _, pos_a, pos_b = data.split(' ')
                pos_a, pos_b = int(pos_a), int(pos_b)

                cards_in_hand = len(self.player.hand.cards)
                if pos_a < 0 or pos_a >= cards_in_hand or pos_b < 0 or pos_b >= cards_in_hand:
                    raise InputValidationException()

                self.player.hand.move(pos_a, pos_b)
                self.print_data(self.player.hand)

            elif re.match('^6 \d+$', data):
                _, pos = data.split(' ')
                pos = int(pos)

                cards_in_hand = len(self.player.hand.cards)
                if pos < 0 or pos >= cards_in_hand:
                    raise InputValidationException()

                self.print_data('You discarded: ', self.player.discard(pos))
                self.print_data(self.player.hand)

            elif re.match('^end$', data):
                ctrl.next_turn()

            elif re.match('^exit$', data):
                ctrl.force_exit = True
            else:
                raise InputValidationException()

        except InputValidationException:
            self.print_data('\nError: Please rekey')


    def process(self):
        from gin.gin_controller import GinController
        ctrl = GinController.get()

        self.print_menu(ctrl)
        data = self.get_input()
        self.input_action(ctrl, data)


class RemoteConsoleGinPlayerInput(ConsoleGinPlayerInput):
    conn = None

    def __init__(self):
        from gin.gin_controller import GinController
        ctrl = GinController.get()

        # self.output_buffer = StringIO()

        HOST = ''                 # Symbolic name meaning all available interfaces
        PORT = 50007              # Arbitrary non-privileged port
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind((HOST, PORT))
        sock.listen(1)
        self.conn, addr = sock.accept()
        ctrl.active_connections.append(self.conn)

        print(addr, 'has connected...')

    def print_data(self, *args, command=None, **kwargs):
        from gin.gin_controller import GinController
        ctrl = GinController.get()

        if not command:
            command = ctrl.COMMANDS['NO_ACTION']

        self.output_buffer = StringIO()
        super(RemoteConsoleGinPlayerInput, self).print_data(*args, command=command, **kwargs)

        self.output_buffer.seek(0)
        data_dict = {
            'data': self.output_buffer.read(),
            'command': command,
        }
        # self.output_buffer.seek(0)
        # self.output_buffer.truncate(0)
        self.output_buffer.close()

        # print('sending: ', data_dict)
        data = pickle.dumps(data_dict)
        self.conn.sendall(data)


    def get_input(self):
        return self.conn.recv(4096).decode('utf-8')
