from django.db import models

from base.controller import Controller

from core.util import obj_to_string, string_to_obj


class Game(models.Model):
    players = models.ManyToManyField('auth.User', related_name='games')
    data    = models.TextField(default='')

    def get_controller(self):
        Controller._ctrl = string_to_obj(self.data) # Weird... Controller._ctrl wasn't preservered in the pickle...
        return Controller.get()

    def set_controller(self, ctrl):
        self.data = obj_to_string(ctrl)
