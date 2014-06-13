import pickle

from django.http import HttpResponse

from core.models import Game


# class MyEncoder(json.JSONEncoder):
#     def default(self, o):
#         return o.__dict__

def obj_to_string(obj):
    byte_data = pickle.dumps(obj)
    int_data = int.from_bytes(byte_data, byteorder='big')
    return str(int_data)

def string_to_obj(string):
    int_data = int(string)
    byte_data = int_data.to_bytes((int_data.bit_length() // 8), byteorder='big')
    return pickle.loads(byte_data)


def index(request):
    from card_game.gin.web.controller import WebGinController as Controller

    print(request.user.id)

    # Game.objects.all().delete()

    db_game, created = request.user.games.get_or_create()
    print(Game.objects.filter(players=request.user))
    print(db_game, created)

    if created:
        print('created')
        ctrl = Controller.get()
        ctrl.create_game()
        # db_game.data = pickle.dumps(ctrl)
        # print(db_game.data)
        # curr_int = int.from_bytes(db_game.data, byteorder='big')
        # print(curr_int)
        # print(curr_int.to_bytes((curr_int.bit_length() // 8), byteorder='big'))

        db_game.data = obj_to_string(ctrl)
        # print(string)
        # print(string_to_obj(string))


        db_game.save()
    else:
        print('found')
        ctrl = string_to_obj(db_game.data)
        # ctrl = pickle.loads(db_game.data)

    print(ctrl.current_player().hand.cards)

    # ctrl = Controller.get()
    # ctrl.create_game()
    # ctrl.main_loop()

    return HttpResponse('Hello')
