
import enum

class Card(object):
  def __init__(self, name, age, cost=None, parents=None, children=None):
    self.name = name
    self.age = age
    self.cost = cost or []
    self.parents = parents or []
    self.children = children or []

class ResourceCard(Card):
  """Brown or gray resource for raw materials or manufactured goods card."""
  def __init__(self, name, age, resources, cost=None, parents=None, children=None):
    super(ResourceCard, self).__init__(name, age, cost=cost, parents=parents, children=children)
    self.resources = resources

class ScienceCard(Card):
  """Green science card."""
  def __init__(self, name, age, science, cost=None, parents=None, children=None):
    super(ScienceCard, self).__init__(name, age, cost=cost, parents=parents, children=children)
    self.science = science

class MilitaryCard(Card):
  """Red military card."""
  def __init__(self, name, age, military, cost=None, parents=None, children=None):
    super(MilitaryCard, self).__init__(name, age, cost=cost, parents=parents, children=children)
    self.military = military

class CivilCard(Card):
  """Blue civilian structures card."""
  def __init__(self, name, age, points, cost=None, parents=None, children=None):
    super(CivilCard, self).__init__(name, age, cost=cost, parents=parents, children=children)
    self.points = points

class CommerceCard(Card):
  """Yellow commerce card."""
  def __init__(self, name, age, commerce_rule, cost=None, parents=None, children=None):
    super(CommerceCard, self).__init__(name, age, cost=cost, parents=parents, children=children)
    self.commerce_rule = commerce_rule

class GuildCard(Card):
  """Purple guild card."""
  def __init__(self, name, age, guild_rule, cost=None, parents=None, children=None):
    super(GuildCard, self).__init__(name, age, cost=cost, parents=parents, children=children)
    self.guild_rule = guild_rule

