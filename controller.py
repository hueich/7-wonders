
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
    self.resetGame()
    self._loadAssets(asset_file)

  def resetGame(self):
    self.players = []
    self.all_cards = []
    self.current_cards = []
    self.wonders = []

  def addPlayer(self, name):
    player = player_lib.Player(name)
    self.players.append(player)
    return len(self.players) - 1

  def setPlayerWonder(self, index, wonder_name):
    wonder = self._getWonder(wonder_name)
    if not wonder:
      raise exception.GameException('Invalid wonder name!')
    self.players[index].wonder = wonder

  def setupGame(self):
    """
    Args:
      players: List of players, in clockwise order.
    """
    self._setupPlayers()
    self._pruneAssets()

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

