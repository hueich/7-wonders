from django.contrib.auth.models import User
from django.db import models


class Game(models.Model):

  class Status(object):
    CREATED = 'CR'
    STARTED = 'ST'
    FINISHED = 'FN'

    choices = (
      (CREATED, 'Created'),
      (STARTED, 'Started'),
      (FINISHED, 'Finished'),
    )

  players = models.ManyToManyField(User, through='Player')
  creator = models.ForeignKey('Player')
  creation_timestamp = models.DateTimeField(auto_now_add=True)

  name = models.CharField(max_length=100)
  status = models.CharField(max_length=2, choices=Status.choices, default=Status.CREATED)
  # phase = models.CharField(max_length=3)  # TODO: Add choices
  # expansions = None  # TODO: Use bit field?
  random_city = models.BooleanField(default=True)
  starting_coins = models.PositiveSmallIntegerField(null=True, blank=True)


class Player(models.Model):

  class Battle(object):
    WIN = 'W'
    LOSS = 'L'
    DEF_AWAY = 'D'
    DEF_BACK = 'B'

  user = models.ForeignKey(User)
  game = models.ForeignKey(Game)
  left = models.OneToOneField('self')
  right = models.OneToOneField('self')
  wonder = models.ForeignKey('Wonder')
  coins = models.PositiveSmallIntegerField()
  battles = models.CharField(max_length=8, blank=True)


class Wonder(models.Model):
  name = models.CharField(max_length=100)
