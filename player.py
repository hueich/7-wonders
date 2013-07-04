
import constants
import exception

class Player(object):
  def __init__(self, name, wonder=None, left=None, right=None, coins=constants.PLAYER_STARTING_COINS):
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
    self.wins = 0
    self.losses = 0
    self.wonder_stage = 0
    self.cards = []
    self.hand = []

  def setHand(self, hand=None):
    """Set the player's cards in hand for selection."""
    self.hand = hand or []

  def canBuildCard(self, card):
    """Check whether the card can be built by the player.

    Args:
      card: The card to build.

    Returns:
      True if the card can be built.
    """
    # TODO
    return True

  def buildCard(self, card):
    """Build the card."""
    if self.canBuildCard(card):
      self.payForCard(card)
      self.hand.remove(card)
      self.cards.append(card)
      self.applyBonus(card)
    else:
      raise exception.IllegalMoveException(self, card, 'Cannot build card.')

  def payForCard(self, card):
    """Pay the cost of the card."""
    pass

  def applyBonus(self, card):
    """Apply the bonus on the card."""
    pass

  def exchangeCard(self, card):
    """Exchange card for coins."""
    self.hand.remove(card)
    self.coins += constants.CARD_EXCHANGE_RATE

  def canBuildWonderStage(self):
    """Check whether the player can build the next wonder stage."""
    if len(self.wonder.stages) == self.wonder_stage:
      return False

    # TODO
    return True

  def buildWonderStage(self, card):
    """Build the next stage of the wonder."""
    if self.canBuildWonderStage():
      self.hand.remove(card)
      self.wonder_stage += 1
    else:
      raise exception.IllegalMoveException(self, card, 'Cannot build wonder stage.')

  def getActiveWonderStages(self):
    return self.wonder.stages[:self.wonder_stage]

  def getMilitaryStrength(self):
    """Get the player's current military strength, used for combat resolution."""
    # TODO
    return 0

  def calcPoints(self):
    """Calculate total points the player has."""
    # TODO
    return 0

class TurnSummary(object):
  def __init__(self, action, card, coin_delta=0):
    self.action = action
    self.card = card
    self.coin_delta = coin_delta
