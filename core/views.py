from django.http import HttpResponse, HttpResponseRedirect

from card_game.gin.web.controller import WebGinController as Controller

from core.models import Game
from core.decorators import manage_controller


def join_game(request, game_id):
    db_game = Game.objects.get(id=game_id)

    assert db_game.players.count() < 2

    player_1 = db_game.players.get()

    db_game.players.add(request.user)

    ctrl = Controller.get()
    ctrl.create_game()

    ctrl.players[0].user = player_1
    ctrl.players[1].user = request.user

    db_game.set_controller(ctrl)
    db_game.save()

    return HttpResponseRedirect('/')

def create_game(request):
    Game.objects.all().delete()

    db_game = request.user.games.create()

    return HttpResponse('{}'.format(db_game.id))

@manage_controller
def index(request, ctrl):
    player = request.user.player
    return HttpResponse('{}'.format(player.hand.cards))

@manage_controller
def view_hand(request, ctrl):
    player = request.user.player
    return HttpResponse('{}'.format(player.hand.cards))

@manage_controller
def draw_deck(request, ctrl):
    drawn = request.user.player.draw_deck()
    return HttpResponse('{}'.format(drawn))

@manage_controller
def draw_pile(request, ctrl):
    drawn = request.user.player.draw_pile()
    return HttpResponse('{}'.format(drawn))

