import json

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from gin.web.controller import WebGinController as Controller
from gin.card import GinCard

from core.models import Game
from core.decorators import manage_controller

class GinEncoder(json.JSONEncoder):
    def default(self, obj):
        # print(obj)
        # print(obj.__class__)
        # print(isinstance(obj, GinCard))

        if isinstance(obj, GinCard):
            # print([obj])
            return {
                'value': obj.value,
                'suit': obj.suit,
            }


            # return [obj.real, obj.imag]

        # Let the base class default method raise the TypeError
        return json.JSONEncoder.default(self, obj)


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
    # return HttpResponse(json.dumps(request.user.player.hand.cards, cls=GinEncoder))
    return render(request, 'core/index.htm')

@manage_controller
def view_hand(request, ctrl):
    return HttpResponse(json.dumps(request.user.player.hand.cards, cls=GinEncoder))

@manage_controller
def draw_deck(request, ctrl):
    drawn = request.user.player.draw_deck()
    return HttpResponse(json.dumps(drawn, cls=GinEncoder))

@manage_controller
def draw_pile(request, ctrl):
    drawn = request.user.player.draw_pile()
    return HttpResponse(json.dumps(drawn, cls=GinEncoder))

@manage_controller
def discard(request, ctrl, card_pos):
    card_pos = int(card_pos)
    discarded = request.user.player.discard(card_pos)
    return HttpResponse(json.dumps(discarded, cls=GinEncoder))

@manage_controller
def view_pile(request, ctrl):
    return HttpResponse(json.dumps(ctrl.get_pile().peek(), cls=GinEncoder))

@manage_controller
def card_pos_swap(request, ctrl, pos_a, pos_b):
    pos_a, pos_b = int(pos_a), int(pos_b)
    request.user.player.hand.move(pos_a, pos_b)
    return HttpResponse(json.dumps(request.user.player.hand.cards, cls=GinEncoder))

