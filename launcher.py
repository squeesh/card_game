class Launcher(object):
    @staticmethod
    def start_game():
        from gin.console.controller import AllLocalGinController as Controller

        print('Welcome to shitty Gin', ' '.join(Controller.SUITS))
        print('Waiting for player to connect...')

        ctrl = Controller.get()
        ctrl.create_game()
        ctrl.main_loop()
