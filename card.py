
import enum

class Card(object):
  def __init__(self, name, age, min_players, bonus, cost=None, parents=None, children=None):
    self.name = name
    self.age = age
    self.min_players = int(min_players)
    self.bonus = bonus
    self.cost = cost if isinstance(cost, dict) else {}
    self.parents = parents if isinstance(parents, list) else []
    self.children = children if isinstance(children, list) else []

  def __eq__(self, other):
    return self.__dict__ == other.__dict__

  def __str__(self):
    return self.__class__.__name__ + ': ' + str(self.__dict__)

  def __repr__(self):
    return '<' + str(self) + '>'

class BasicResourceCard(Card):
  """Brown resource card for raw materials."""
  pass

class AdvResourceCard(Card):
  """Gray resource card for manufactured goods."""
  pass

class ScienceCard(Card):
  """Green science card."""
  pass

class MilitaryCard(Card):
  """Red military card."""
  pass

class CivilCard(Card):
  """Blue civilian structures card."""
  pass

class CommerceCard(Card):
  """Yellow commerce card."""
  pass

class GuildCard(Card):
  """Purple guild card."""
  pass
