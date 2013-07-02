
class Game(object):

  def __init__(self, players):
    """
    Args:
      players: List of players, given in clockwise order."
    """
    self.players = players
    self.updatePlayerPositions()

  def updatePlayerPositions(self):
    """Update players' relative positions to each other."""
    prev_player = None
    for player in self.players:
      if prev_player is None:
        prev_player = player
      else:
        player.right = prev_player
        prev_player.left = player
        prev_player = player
    # Connect first and last player
    self.players[0].right = self.players[-1]
    self.players[-1].left = self.players[0]

  def doCombat(self):
    pass
