
import constants
import loader
import utils

DEFAULT_ASSET_FILE = 'res/original.7wr'

class Game(object):

  def __init__(self):
    self.players = []
    self.all_cards = []
    self.all_wonders = []

  def setupGame(self, players, asset_file=None):
    """
    Args:
      players: List of players, in clockwise order.
      asset_file: Path to asset file.
    """
    self._setupPlayers(players)
    self._loadAssets(asset_file)
    self._pruneAssets()

  def _setupPlayers(self, players):
    self.players = players
    utils.updatePlayerRelations(self.players)

  def _loadAssets(self, asset_file):
    asset_file = asset_file or DEFAULT_ASSET_FILE
    with open(asset_file, 'r') as fp:
      assets = loader.loadAssets(fp)
    self.all_cards = assets[constants.CARDS_KEY]
    self.all_wonders = assets[constants.WONDERS_KEY]

  def _pruneAssets(self):
    num_players = len(self.players)
    # TODO

  def doCombat(self):
    pass
