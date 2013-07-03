import constants
import utils

class BaseBenefit(object):
  def build(self, player):
    pass

  def getPoints(self, player):
    return 0

class PointBenefit(BaseBenefit):
  def __init__(self, points):
    self.points = points

class ResourceBenefit(BaseBenefit):
  def __init__(self, resources):
    """
    Args:
      resources: A list of resources this benefit provides. Duplicates are ok.
        For multiple-choice resources, use a tuple containing the choices.
    """
    self.resources = resources

class ScienceBenefit(BaseBenefit):
  def __init__(self, science):
    """
    Args:
      science: The science this benefit provides. For multiple-choice, use a tuple containing the choices.
    """
    self.science = science

class MilitaryBenefit(BaseBenefit):
  def __init__(self, shields):
    self.shields = shields

class TradingBenefit(BaseBenefit):
  def __init__(self, resources, relations, cost=constants.COMMERCE_TRADING_RATE):
    """
    Args:
      resources: A list of tradable resources.
      relations: A list of player relations.
      cost: Cost per resource being traded.
    """
    self.resources = resources
    self.relations = relations
    self.cost = cost

class CountedBenefit(BaseBenefit):
  def __init__(self, relations):
    self.relations = relations

  def getCount(self, player):
    return utils.countAssets(player, self.relations, self.assetFilter)

  @staticmethod
  def assetFilter(player):
    raise NotImplementedError()

class CardBenefit(CountedBenefit):
  def __init__(self, relations, card_type, points_per_card=0, coins_per_card=0):
    super(CardBenefit, self).__init__(relations)
    self.card_type = card_type
    self.points_per_card = points_per_card
    self.coins_per_card = coins_per_card

class WonderBenefit(CountedBenefit):
  def __init__(self, relations, points_per_stage, coins_per_stage=0):
    super(WonderBenefit, self).__init__(relations)
    self.points_per_stage = points_per_stage
    self.coins_per_stage = coins_per_stage

class DefeatBenefit(CountedBenefit):
  def __init__(self, relations, points_per_defeat):
    super(DefeatBenefit, self).__init__(relations)
    self.points_per_defeat = points_per_defeat
