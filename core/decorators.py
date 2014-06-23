from core.util import string_to_obj


def manage_controller(func):
    def inner(request, *args, **kwargs):
        # from time import sleep
        # sleep(5)

        # TODO: Test data
        from django.contrib.auth import authenticate
        user = authenticate(username='squoosh', password='a')
        request.user = user
        #### end todo ####

        db_game = request.user.games.get()
        ctrl = db_game.get_controller()
        request.player   = ctrl.get_player_for_user(request.user)
        request.opponent = ctrl.get_opponent_for_user(request.user)

        response = func(request, ctrl=ctrl, *args, **kwargs)

        db_game.set_controller(ctrl)
        db_game.save()

        return response

    return inner