class Launcher(object):
    @staticmethod
    def start_game():
        from gin.gin_controller import BaseGinController, GinController

        print('Welcome to shitty Gin', ' '.join(BaseGinController.SUITS))
        print('Waiting for player to connect...')

        ctrl = GinController.get()
        ctrl.create_game()
        ctrl.main_loop()
