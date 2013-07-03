import enum
import exception

def getCardsOfType(cards, card_type):
  return [c for c in cards if isinstance(c, card_type)]

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
