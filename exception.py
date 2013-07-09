import exceptions

class GameException(exceptions.Exception):
  pass

class IllegalMoveException(GameException):
  def __init__(self, player, card, msg=''):
    self.player = player
    self.card = card
    self.msg = msg

class ParseError(GameException):
  def __init__(self, field, msg=''):
    self.field = field
