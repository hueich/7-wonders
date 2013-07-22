
import constants
import loader
import player as player_lib
import utils

DEFAULT_ASSET_FILE = 'res/original.7wr'

class Game(object):

  def __init__(self, asset_file=None):
    """
    Args:
      asset_file: Path to asset file.
    """
    self.reset()
    self._loadAssets(asset_file)

  def reset(self):
    self.players = []
    self.all_cards = []
    self.current_cards = []
    self.wonders = []

  def addPlayer(self, name):
    """Add a player to the game. Order matters, so add in clockwise order.

    Args:
      name: Name of the player.

    Returns:
      Index position of the newly added player.
    """
    player = player_lib.Player(name)
    self.players.append(player)
    return len(self.players) - 1

  def setupGame(self):
    """Set up the game after players have been added."""
    self._setupPlayers()
    self._pruneAssets()

  def setPlayerWonder(self, index, wonder_name):
    """Set the player's wonder board.

    Args:
      index: Index position of the player.
      wonder_name: Name of the wonder for the player.
    """
    wonder = self._getWonder(wonder_name)
    if not wonder:
      raise exception.GameException('Invalid wonder name!')
    self.players[index].wonder = wonder

  def _setupPlayers(self):
    utils.updatePlayerRelations(self.players)

  def _loadAssets(self, asset_file):
    asset_file = asset_file or DEFAULT_ASSET_FILE
    with open(asset_file, 'r') as fp:
      assets = loader.loadAssets(fp)
    self.all_cards = assets[constants.CARDS_KEY]
    self.wonders = assets[constants.WONDERS_KEY]

  def _pruneAssets(self):
    num_players = len(self.players)
    # TODO

  def _getWonder(self, name):
    for wonder in self.wonders:
      if wonder.name == name:
        return wonder
    return None

  def doCombat(self):
    pass


class Launcher(object):
  def __init__(self, asset_file=None):
    self.game = Game(asset_file)

