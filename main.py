from gin.gin_controller import GinController

ctrl = GinController.get()
ctrl.create_game()
ctrl.main_loop()
