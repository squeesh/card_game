from django.db import models

class Game(models.Model):
    players = models.ManyToManyField('auth.User', related_name='games')
    data    = models.TextField(default='')