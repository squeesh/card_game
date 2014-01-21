from abc import ABCMeta

class Controller(object, metaclass=ABCMeta):
    _ctrl = None
    players = None
    active_player = None
    force_exit = False
    active_connections = None

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
                for conn in self.active_connections:
                    conn.close()
                break
