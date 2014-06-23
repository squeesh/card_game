import hashlib

from django.db import models

from base.controller import Controller

from core.util import obj_to_string, string_to_obj


class Game(models.Model):
    players = models.ManyToManyField('auth.User', related_name='games', through='core.PlayerGame')
    data    = models.TextField(default='')
    hash    = models.CharField(max_length=64, default='')

    def get_controller(self):
        Controller._ctrl = string_to_obj(self.data) # Weird... Controller._ctrl wasn't preservered in the pickle...
        return Controller.get()

    def set_controller(self, ctrl):
        self.data = obj_to_string(ctrl)

        sha = hashlib.sha224()
        sha.update(self.data.encode('utf-8'))
        self.hash = sha.hexdigest()


class PlayerGame(models.Model):
    class Meta:
        unique_together = ('player', 'game')

    player  = models.ForeignKey('auth.User', unique=True)
    game    = models.ForeignKey('core.Game')
