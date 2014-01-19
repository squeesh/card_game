from abc import ABCMeta

class Controller(object, metaclass=ABCMeta):
    _ctrl = None
    board = None

    def __init__(self):
        assert not self._ctrl

    @classmethod
    def get(cls):
        if not cls._ctrl:
            cls._ctrl = cls()

        return cls._ctrl

    def main_loop(self):
        pass
