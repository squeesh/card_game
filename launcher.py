class Launcher(object):
    @staticmethod
    def start_game():
        from gin.multiplayer.controller import LocalRemoteGinController

        print('Welcome to shitty Gin', ' '.join(LocalRemoteGinController.SUITS))
        print('Waiting for player to connect...')

        ctrl = LocalRemoteGinController.get()
        ctrl.create_game()
        ctrl.main_loop()
