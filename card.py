
import enum

class Card(object):
  def __init__(self, name, age, benefit, cost=None, parents=None, children=None):
    self.name = name
    self.age = age
    self.benefit = benefit
    self.cost = cost or []
    self.parents = parents or []
    self.children = children or []

  def __eq__(self, other):
    return self.__dict__ == other.__dict__

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
