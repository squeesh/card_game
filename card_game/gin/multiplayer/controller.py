from gin.controller import GinController
from gin.multiplayer.player import RemoteGinPlayer
from gin.player import GinPlayer


class LocalRemoteGinController(GinController):
    COMMANDS = {
        'NO_ACTION': '0',
        'GET_INPUT': '1',
        'KILL_CONN': '2',
    }

    def __init__(self, *args, **kwargs):
        super(LocalRemoteGinController, self).__init__(*args, **kwargs)
        self.active_connections = []

    def get_new_players(self, deck):
        return (GinPlayer(deck.draw_many(11), 1), RemoteGinPlayer(deck.draw_many(11), 2))

    def exit_game(self):
        for conn in self.active_connections:
            data_dict = {
                'data': '',
                'command': self.COMMANDS['KILL_CONN'],
            }

            data = pickle.dumps(data_dict)
            conn.sendall(data)
            conn.close()
