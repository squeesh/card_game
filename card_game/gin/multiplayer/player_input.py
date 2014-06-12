from io import StringIO
import pickle
import socket

import settings

from base.controller import Controller

from gin.console.player_input import ConsoleGinPlayerInput


class RemoteConsoleGinPlayerInput(ConsoleGinPlayerInput):
    conn = None

    def __init__(self):
        ctrl = Controller.get()

        # self.output_buffer = StringIO()

        HOST = settings.REMOTE_HOST
        PORT = settings.REMOTE_PORT
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind((HOST, PORT))
        sock.listen(1)
        self.conn, addr = sock.accept()
        ctrl.active_connections.append(self.conn)

        print(addr, 'has connected...')

    def print_data(self, *args, command=None, **kwargs):
        ctrl = Controller.get()

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
