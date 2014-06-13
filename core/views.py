import pickle

from django.http import HttpResponse, HttpResponseRedirect

from core.models import Game

from card_game.gin.web.controller import WebGinController as Controller


def obj_to_string(obj):
    byte_data = pickle.dumps(obj)
    hex_string = hex(int.from_bytes(byte_data, byteorder='big'))
    return hex_string

def string_to_obj(string):
    int_data = int(string, 16)
    byte_data = int_data.to_bytes((int_data.bit_length() // 8), byteorder='big')
    return pickle.loads(byte_data)

def index(request):
    db_game = request.user.games.get()
    ctrl = string_to_obj(db_game.data)
    player = ctrl.get_player_for_user(request.user)

    return HttpResponse('{}'.format(player.hand.cards))

def join_game(request, game_id):
    db_game = Game.objects.get(id=game_id)
    print(db_game.players.count())

    assert db_game.players.count() < 2

    player_1 = db_game.players.get()

    db_game.players.add(request.user)

    ctrl = Controller.get()
    ctrl.create_game()

    ctrl.players[0].user = player_1
    ctrl.players[1].user = request.user

    db_game.data = obj_to_string(ctrl)
    db_game.save()

    return HttpResponseRedirect('/')

def create_game(request):
    Game.objects.all().delete()

    db_game = request.user.games.create()

    return HttpResponse('{}'.format(db_game.id))
