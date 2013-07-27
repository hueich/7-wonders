
import random

import card as card_lib
import constants
import enum
import loader
import player as player_lib
import utils

DEFAULT_ASSET_FILE = 'res/original.7wr'

class Game(object):

  def __init__(self):
    self.reset()

  def reset(self):
    self._players = []
    self._wonders = []
    self._all_cards = []
    self._age1_cards = []
    self._age2_cards = []
    self._age3_cards = []
    self._discarded_cards = []

  def addPlayer(self, name):
    """Add a player to the game. Order matters, so add in clockwise order.

    Args:
      name: Name of the player.

    Returns:
      Index position of the newly added player.
    """
    player = player_lib.Player(name)
    self._players.append(player)
    return len(self._players) - 1

  def loadAssets(self, asset_file):
    """Load assets from a file.

    Args:
      asset_file: Path to asset file.
    """
    with open(asset_file, 'r') as fp:
      assets = loader.loadAssets(fp)
    self._all_cards = assets[constants.CARDS_KEY]
    self._wonders = assets[constants.WONDERS_KEY]

  def setupGame(self):
    """Set up the game after players have been added."""
    self._setupPlayers()
    self._setupAssets()

  def setPlayerWonder(self, index, wonder_name):
    """Set the player's wonder board.

    Args:
      index: Index position of the player.
      wonder_name: Name of the wonder for the player.
    """
    wonder = self._getWonder(wonder_name)
    if not wonder:
      raise exception.GameException('Invalid wonder name!')
    self._players[index].wonder = wonder

  def _setupPlayers(self):
    utils.updatePlayerRelations(self._players)

  def _setupAssets(self):
    """Setup the card decks."""
    self._selectGuildCards()
    pruned_cards = self._pruneCardsByNumPlayers()
    self._partitionCards(pruned_cards)

  def _selectGuildCards(self):
    """Randomly select a number of guild cards base on number of players, and put them into Age III card list."""
    all_guild_cards = utils.getCardsOfType(self._all_cards, card_lib.GuildCard)
    random.shuffle(all_guild_cards)
    num_guild_cards_to_select = utils.getNumGuildCards(self.getNumPlayers())
    selected_guild_cards = all_guild_cards[:num_guild_cards_to_select]
    self._age3_cards.extend(selected_guild_cards)

  def _pruneCardsByNumPlayers(self):
    """Prune the list of all cards according to number of players.

    Returns:
      List of cards with minimum number of players less than or equal to current number of players.
    """
    num_players_range = range(self.getNumPlayers() + 1)
    return [card for card in self._all_cards if card.min_players in num_players_range]

  def _partitionCardsIntoAges(self, input_cards):
    """Partition the given list of cards into ages."""
    for card in input_cards:
      if card.age == enum.Age.I:
        self._age1_cards.append(card)
      elif card.age == enum.Age.II:
        self._age2_cards.append(card)
      elif card.age == enum.Age.III:
        self._age3_cards.append(card)

  def _getWonder(self, name):
    for wonder in self._wonders:
      if wonder.name == name:
        return wonder
    return None

  def beginAge1(self):
    pass

  def _shuffleAndDeal(self, cards, num_stacks):
    stack_size = int(len(cards) / num_stacks)
    random.shuffle(cards)
    stacks = []
    for i in xrange(num_stacks):
      stacks.append(cards[i*stack_size:(i+1)*stack_size])
    return stacks

  def getNumPlayers(self):
    return len(self._players)

  def doCombat(self):
    pass


class Launcher(object):
  def __init__(self, asset_file=None):
    self._asset_file = asset_file or DEFAULT_ASSET_FILE
    self._game = Game()

