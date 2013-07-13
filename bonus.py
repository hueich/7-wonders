import constants
import utils

class BaseBonus(object):
  def build(self, player):
    pass

  def getPoints(self, player):
    return 0

  def __eq__(self, other):
    return self.__dict__ == other.__dict__

  def __str__(self):
    return self.__class__.__name__ + ': ' + str(self.__dict__)

  def __repr__(self):
    return '<' + str(self) + '>'

class PointBonus(BaseBonus):
  def __init__(self, points):
    self.points = int(points)

class ResourceBonus(BaseBonus):
  def __init__(self, resources, tradable=None):
    """
    Args:
      resources: A list of resources this bonus provides. Duplicates are ok.
        For multiple-choice resources, use a tuple containing the choices.
      tradable: Whether the resource can be traded/bought by neighbors.
    """
    self.resources = resources
    self.tradable = True if tradable is None else tradable

class ScienceBonus(BaseBonus):
  def __init__(self, science):
    """
    Args:
      science: The science this bonus provides. For multiple-choice, use a tuple containing the choices.
    """
    self.science = science

class MilitaryBonus(BaseBonus):
  def __init__(self, shields):
    self.shields = int(shields)

class TradingBonus(BaseBonus):
  def __init__(self, resources, relations, cost=None):
    """
    Args:
      resources: A list of tradable resources.
      relations: A list of player relations.
      cost: Cost per resource being traded.
    """
    self.resources = resources
    self.relations = relations
    self.cost = constants.COMMERCE_TRADING_RATE if cost is None else int(cost)

class BaseCountBonus(BaseBonus):
  """Abstract class for bonuses that need to count something, e.g. cards, wonder stages, etc."""
  def __init__(self, relations):
    self.relations = relations

  def getCount(self, player):
    return utils.countAssets(player, self.relations, self.assetFilter)

  def assetFilter(self, player):
    raise NotImplementedError()

class CardCountBonus(BaseCountBonus):
  def __init__(self, relations, card_type, points_per_card=None, coins_per_card=None):
    super(CardCountBonus, self).__init__(relations)
    self.card_type = card_type
    self.points_per_card = 0 if points_per_card is None else int(points_per_card)
    self.coins_per_card = 0 if coins_per_card is None else int(coins_per_card)

  def assetFilter(self, player):
    return utils.getCardsOfType(player.cards, self.card_type)

class WonderCountBonus(BaseCountBonus):
  def __init__(self, relations, points_per_stage, coins_per_stage=None):
    super(WonderCountBonus, self).__init__(relations)
    self.points_per_stage = points_per_stage
    self.coins_per_stage = 0 if coins_per_stage is None else int(coins_per_stage)

  def assetFilter(self, player):
    return player.getActiveWonderStages()

class DefeatCountBonus(BaseCountBonus):
  def __init__(self, relations, points_per_defeat):
    super(DefeatCountBonus, self).__init__(relations)
    self.points_per_defeat = points_per_defeat
