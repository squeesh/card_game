import re
from io import StringIO
import sys

from exceptions import InputValidationException
from player_input import PlayerInput



class ConsoleGinPlayerInput(PlayerInput):
    output_buffer = sys.stdout

    def get_input(self):
        return input('Command: ')

    def print_menu(self):
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
""".format(self.player.player_num), file=self.output_buffer
        )

    def input_action(self, ctrl, data):
        try:
            if re.match('^1$', data):
                print(self.player.hand, file=self.output_buffer)

            elif re.match('^2$', data):
                if ctrl.board.pile.cards:
                    print(ctrl.board.pile.cards[0], file=self.output_buffer)
                else:
                    print('Pile is empty', file=self.output_buffer)

            elif re.match('^3$', data):
                drawn = ctrl.board.deck.draw()
                self.player.hand.add(drawn)
                print('You drew: ', drawn, file=self.output_buffer)

            elif re.match('^4$', data):
                if ctrl.board.pile.cards:
                    drawn = ctrl.board.pile.draw()
                    self.player.hand.add(drawn)
                    print('You drew: ', drawn, file=self.output_buffer)
                else:
                    print('Error: Pile empty', file=self.output_buffer)

            elif re.match('^5 \d+ \d+$', data):
                _, pos_a, pos_b = data.split(' ')
                pos_a, pos_b = int(pos_a), int(pos_b)

                cards_in_hand = len(self.player.hand.cards)
                if pos_a < 0 or pos_a >= cards_in_hand or pos_b < 0 or pos_b >= cards_in_hand:
                    raise InputValidationException()

                self.player.hand.move(pos_a, pos_b)
                print(self.player.hand, file=self.output_buffer)

            elif re.match('^6 \d+$', data):
                _, pos = data.split(' ')
                pos = int(pos)

                cards_in_hand = len(self.player.hand.cards)
                if pos < 0 or pos >= cards_in_hand:
                    raise InputValidationException()

                print('You discarded: ', self.player.discard(pos), file=self.output_buffer)
                print(self.player.hand, file=self.output_buffer)

            elif re.match('^end$', data):
                ctrl.next_turn()

            elif re.match('^exit$', data):
                ctrl.force_exit = True
            else:
                raise InputValidationException()

        except InputValidationException:
            print(file=self.output_buffer)
            print('Error: Please rekey', file=self.output_buffer)


    def process(self):
        from gin.gin_controller import GinController
        ctrl = GinController.get()

        self.print_menu()
        data = self.get_input()
        self.input_action(ctrl, data)


class RemoteConsoleGinPlayerInput(ConsoleGinPlayerInput):
    conn = None

    def __init__(self):
        from gin.gin_controller import GinController
        ctrl = GinController.get()

        self.output_buffer = StringIO()
        import socket

        HOST = ''                 # Symbolic name meaning all available interfaces
        PORT = 50007              # Arbitrary non-privileged port
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind((HOST, PORT))
        sock.listen(1)
        self.conn, addr = sock.accept()
        ctrl.active_connections.append(self.conn)

        print('Connected by', addr)


    def get_input(self):
        data = self.conn.recv(1024).decode('utf-8')
        return data

    def print_menu(self):
        super(RemoteConsoleGinPlayerInput, self).print_menu()
        self.output_buffer.seek(0)
        self.conn.sendall(bytearray(self.output_buffer.read(), 'utf-8'))
        self.output_buffer.truncate(0)

    def input_action(self, ctrl, data):
        super(RemoteConsoleGinPlayerInput, self).input_action(ctrl, data)
        self.output_buffer.seek(0)
        self.conn.sendall(bytearray(self.output_buffer.read(), 'utf-8'))
        self.output_buffer.truncate(0)
