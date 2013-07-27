
import enum
import exception

def getCardsOfType(cards, card_type):
  return [c for c in cards if isinstance(c, card_type)]

def getCardsOfAge(cards, age):
  return [c for c in cards if c.age == age]

def countAssets(player, relations, asset_filter):
  count = 0
  for rel in relations:
    cur_player = None
    if rel == enum.Relation.SELF:
      cur_player = player
    elif rel == enum.Relation.LEFT:
      cur_player = player.left
    elif rel == enum.Relation.RIGHT:
      cur_player = player.right
    else:
      raise exception.GameException('Unrecognized relation: %s' % rel)
    count += len(asset_filter(cur_player))
  return count

def updatePlayerRelations(players):
  """Update players' relative positions to each other."""
  prev_player = None
  for player in players:
    if prev_player is None:
      prev_player = player
    else:
      player.right = prev_player
      prev_player.left = player
      prev_player = player
  # Connect first and last player
  players[0].right = players[-1]
  players[-1].left = players[0]

def getNumGuildCards(num_players):
  """Get the number of guild cards to use given the number of players."""
  return num_players + 2

