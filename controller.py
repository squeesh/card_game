from abc import ABCMeta
import pickle

class Controller(object, metaclass=ABCMeta):
    _ctrl = None

    players         = None
    active_player   = None

    force_exit          = False
    active_connections  = None

    COMMANDS = {
        'NO_ACTION': '0',
        'GET_INPUT': '1',
        'KILL_CONN': '2',
    }

    def __init__(self):
        assert not self._ctrl
        self.active_connections = []

    @classmethod
    def get(cls):
        if not cls._ctrl:
            cls._ctrl = cls()

        return cls._ctrl

    def current_player(self):
        return self.players[self.active_player]

    def next_turn(self):
        self.active_player = (self.active_player + 1) % len(self.players)

    def main_loop(self):
        while True:
            self.current_player().process_input()

            if self.force_exit:
                break

        self.exit_game()

    def exit_game(self):
        for conn in self.active_connections:
            data_dict = {
                'data': '',
                'command': self.COMMANDS['KILL_CONN'],
            }

            data = pickle.dumps(data_dict)
            conn.sendall(data)
            conn.close()

