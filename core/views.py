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
    return HttpResponse('{}'.format(request.user.player.hand.cards))

@manage_controller
def view_hand(request, ctrl):
    return HttpResponse('{}'.format(request.user.player.hand.cards))

@manage_controller
def draw_deck(request, ctrl):
    drawn = request.user.player.draw_deck()
    return HttpResponse('{}'.format(drawn))

@manage_controller
def draw_pile(request, ctrl):
    drawn = request.user.player.draw_pile()
    return HttpResponse('{}'.format(drawn))

@manage_controller
def discard(request, ctrl, card_pos):
    card_pos = int(card_pos)
    discarded = request.user.player.discard(card_pos)
    return HttpResponse('{}'.format(discarded))

@manage_controller
def view_pile(request, ctrl):
    return HttpResponse('{}'.format(ctrl.get_pile().peek()))

@manage_controller
def card_pos_swap(request, ctrl, pos_a, pos_b):
    pos_a, pos_b = int(pos_a), int(pos_b)
    request.user.player.hand.move(pos_a, pos_b)
    return HttpResponse('{}'.format(request.user.player.hand.cards))
