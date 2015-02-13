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

  creation_timestamp = models.DateTimeField(auto_now_add=True)
  creator = models.ForeignKey('Player')
  players = models.ManyToManyField(User, through='Player')
  cards = models.ManyToManyField('Card', through='GameCard')

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


class Card(models.Model):
  pass


class GameCard(models.Model):

  class Status(object):
    NONE = 'N'
    HAND = 'H'
    DISCARD = 'D'
    BUILD = 'B'
    WONDER = 'W'

  game = models.ForeignKey(Game)
  card = models.ForeignKey(Card)
  starting_player = models.ForeignKey(Player)
  current_player = models.ForeignKey(Player)
  status = models.CharField(max_length=1, choices=Status.choices, default=Status.NONE)


class Move(models.Model):
  pass
