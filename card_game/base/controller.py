from abc import ABCMeta
import pickle


class Controller(object, metaclass=ABCMeta):
    _ctrl = None

    players         = None
    active_player   = None

    force_exit      = False

    COMMANDS = {
        'NO_ACTION': '0',
        'GET_INPUT': '1',
    }

    def __init__(self):
        assert not self._ctrl

    @classmethod
    def get(cls):
        if not Controller._ctrl:
            Controller._ctrl = cls()

        return Controller._ctrl

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
        pass


