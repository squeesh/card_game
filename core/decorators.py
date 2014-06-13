from core.util import string_to_obj


def manage_controller(func):
    def inner(request, *args, **kwargs):
        db_game = request.user.games.get()
        ctrl = db_game.get_controller()
        request.user.player = ctrl.get_player_for_user(request.user)

        response = func(request, ctrl=ctrl, *args, **kwargs)

        db_game.set_controller(ctrl)
        db_game.save()

        return response

    return inner