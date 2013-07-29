
import itertools
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
    self._eligible_cards = []
    self._guild_cards = []
    self._discarded_cards = []
    self._current_age = enum.Age.I
    self._resetRoundCount()
    self._max_round = None

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
    self._eligible_cards.extend(self._pruneCardsByNumPlayers())

  def _selectGuildCards(self):
    """Randomly select a number of guild cards based on number of players, and put them into guild cards list."""
    all_guild_cards = utils.getCardsOfType(self._all_cards, card_lib.GuildCard)
    random.shuffle(all_guild_cards)
    num_guild_cards_to_select = utils.getNumGuildCards(self.getNumPlayers())
    selected_guild_cards = all_guild_cards[:num_guild_cards_to_select]
    self._guild_cards.extend(selected_guild_cards)

  def _pruneCardsByNumPlayers(self):
    """Prune the list of all cards according to number of players.

    Returns:
      List of cards with minimum number of players less than or equal to current number of players.
    """
    num_players_range = range(self.getNumPlayers() + 1)
    return [card for card in self._all_cards if card.min_players in num_players_range]

  def _getWonder(self, name):
    for wonder in self._wonders:
      if wonder.name == name:
        return wonder
    return None

  def beginRound(self):
    if self._isStartOfAge():
      cards = utils.getCardsOfAge(self._eligible_cards, self._current_age)
      if self._current_age == enum.Age.III:
        cards.extend(self._guild_cards)
      stacks = utils.shuffleAndDeal(cards, self.getNumPlayers())
      for stack, player in zip(stacks, self.players):
        player.setHand(stack)
      self._max_round = len(stacks[0]) - 1

    self._current_round += 1

  def processRound(self):
    for player in self.players:
      self._applyAction(player)

    if self._isEndOfAge():
      # Discard remaining cards.

      # TODO: Handle card resurrection ability.

      # Combat resolution.
      self.resolveMilitaryConflicts()

      # Set next age.
      self._current_age = utils.getNextAge(self._current_age)
      if not self._current_age:
        # TODO: End of the game, do scoring or something.
        pass

      self._resetRoundCount()

  def _resetRoundCount(self):
    self._current_round = 0

  def _isStartOfAge(self):
    return not self._current_round

  def _isEndOfAge(self):
    return self._current_round >= self._max_round

  def _applyAction(self, player):
    pass

  def getNumPlayers(self):
    return len(self._players)

  def resolveMilitaryConflicts(self):
    win_pts = constants.MILITARY_WIN_POINTS_BY_AGE[self._current_age]
    for p1, p2 in itertools.combinations(self._players, 2):
      utils.resolveCombat(p1, p2, win_pts)

class Launcher(object):
  def __init__(self, asset_file=None):
    self._asset_file = asset_file or DEFAULT_ASSET_FILE
    self._game = Game()

