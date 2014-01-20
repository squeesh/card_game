class Launcher(object):
    @staticmethod
    def start_game():
        from gin.gin_controller import BaseGinController, GinController#, ServerGinController, ClientGinController

        print('Welcome to shitty Gin', ' '.join(BaseGinController.SUITS))

        # if not settings.ALLOW_REMOTE:
        ctrl = GinController.get()
        ctrl.create_game()
#         else:
#             print("""
# 1   | Host game
# 2   | Join game
#                 """)
#             data = input('Command: ')

#             if data == "1":
#                 ctrl = ServerGinController.get()
#                 ctrl.create_game()

#             elif data == "2":
#                 ctrl = ClientGinController.get()
#                 ctrl.create_game()



        ctrl.main_loop()

