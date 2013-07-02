
import constants

class Player(object):
  def __init__(self, name, wonder, left=None, right=None, coins=constants.STARTING_COINS):
    """
    Args:
      name: String for the name of the player.
      left: Reference to the player to the left of current player.
      right: Reference to the player to the right of current player.
      wonder: Reference to this player's wonder.
      coins: Starting number of coins.
    """
    self.name = name
    self.left = left
    self.right = right
    self.wonder = wonder
    self.coins = coins
    self.military_points = 0
    self.cards = []
    self.wonder_stage = 0

  def getMilitaryStrength(self):
    """Get the player's current military strength, used for combat resolution."""
    # TODO
    return 0

  def canBuildCard(self, card):
    """Check whether the card can be built by the player.

    Args:
      card: The card to build.

    Returns:
      True if the card can be built.
    """
    pass

  def buildCard(self, card):
    """Build the card."""
    pass

  def exchangeCard(self, card):
    """Exchange card for coins."""
    self.coins += constants.EXCHANGE_RATE

  def buildWonderStage(self, card):
    """Build the next stage of the wonder."""
    pass

  def getActiveWonderStages(self):
    return self.wonder.stages[:self.wonder_stage]

  def calcPoints(self):
    # TODO
    return 0
