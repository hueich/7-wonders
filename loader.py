import json

import bonus as bonus_lib
import card as card_lib
import constants
import enum
import exception
import wonder as wonder_lib

def loadAssets(fp):
  output = json.load(fp)
  assets = {
    constants.CARDS_KEY: _parseCards(output[constants.CARDS_KEY]),
    constants.WONDERS_KEY: _parseWonders(output[constants.WONDERS_KEY])
  }
  return assets

def _parseCards(cards):
  output = []
  for card_info in cards:
    _parseCard(card_info, output)
  return output

def _parseCard(card_info, cards_list):
  for min_players in [int(c) for c in card_info['min_players']]:
    card_type = _parseEnum(card_info['type'], enum.CardType, 'card.type')

    name = str(card_info['name'])
    if not name:
      raise exception.ParseError('card.name')

    age = _parseEnum(card_info['age'], enum.Age, 'card.age')

    bonus = _parseBonus(card_info['bonus'])

    cost = _parseCost(card_info['cost'])

    parents = _getStringListOrNone(card_info, 'parents')
    children = _getStringListOrNone(card_info, 'children')

    card_class = _getCardClassFromString(card_type)

    card = card_class(name, age, min_players, bonus, cost, parents, children)
    cards_list.append(card)

def _getCardClassFromString(card_type):
  card_class = None
  if card_type == enum.CardType.BASIC_RES:
    card_class = card_lib.BasicResourceCard
  elif card_type == enum.CardType.ADV_RES:
    card_class = card_lib.AdvResourceCard
  elif card_type == enum.CardType.SCIENCE:
    card_class = card_lib.ScienceCard
  elif card_type == enum.CardType.MILITARY:
    card_class = card_lib.MilitaryCard
  elif card_type == enum.CardType.CIVIL:
    card_class = card_lib.CivilCard
  elif card_type == enum.CardType.COMMERCE:
    card_class = card_lib.CommerceCard
  elif card_type == enum.CardType.GUILD:
    card_class = card_lib.GuildCard
  else:
    raise exception.ParseError('card.type')
  return card_class

def _parseBonus(bonus_info):
  bonus_type = _parseEnum(bonus_info['type'], enum.BonusType, 'bonus.type')
  bonus = None
  if bonus_type == enum.BonusType.POINT:
    points = int(bonus_info['points'])
    bonus = bonus_lib.PointBonus(points)
  elif bonus_type == enum.BonusType.RESOURCE:
    resources = _parseResources(bonus_info['resources'])
    bonus = bonus_lib.ResourceBonus(resources)
  elif bonus_type == enum.BonusType.SCIENCE:
    science = _parseEnum(bonus_info['science'], enum.Science, 'bonus.science')
    bonus = bonus_lib.ScienceBonus(science)
  elif bonus_type == enum.BonusType.MILITARY:
    shields = int(bonus_info['shields'])
    bonus = bonus_lib.MilitaryBonus(shields)
  elif bonus_type == enum.BonusType.TRADING:
    resources = _parseResources(bonus_info['resources'])
    relations = _parseRelations(bonus_info['relations'])
    cost = _getIntOrNone(bonus_info, 'cost')
    bonus = bonus_lib.TradingBonus(resources=resources, relations=relations, cost=cost)
  elif bonus_type == enum.BonusType.CARD_COUNT:
    relations = _parseRelations(bonus_info['relations'])
    card_type = _getCardClassFromString(bonus_info['card_type'])
    points_per_card = _getIntOrNone(bonus_info, 'points_per_card')
    coins_per_card = _getIntOrNone(bonus_info, 'coins_per_card')
    bonus = bonus_lib.CardCountBonus(relations=relations, card_type=card_type, points_per_card=points_per_card, coins_per_card=coins_per_card)
  elif bonus_type == enum.BonusType.WONDER_COUNT:
    relations = _parseRelations(bonus_info['relations'])
    points_per_stage = _getIntOrNone(bonus_info, 'points_per_stage')
    coins_per_stage = _getIntOrNone(bonus_info, 'coins_per_stage')
    bonus = bonus_lib.WonderCountBonus(relations=relations, points_per_stage=points_per_stage, coins_per_stage=coins_per_stage)
  elif bonus_type == enum.BonusType.DEFEAT_COUNT:
    relations = _parseRelations(bonus_info['relations'])
    points_per_defeat = _getIntOrNone(bonus_info, 'points_per_defeat')
    bonus = bonus_lib.DefeatCountBonus(relations=relations, points_per_defeat=points_per_defeat)
  else:
    raise exception.ParseError('bonus.type')
  return bonus

def _getIntOrNone(dct, key):
  return int(dct[key]) if key in dct else None

def _getStringListOrNone(dct, key):
  return [str(item) for item in dct[key]] if key in dct else None

def _parseEnum(value, enum_type, field):
  if value in enum_type.values:
    return value
  else:
    raise exception.ParseError(field)

def _parseCost(cost_info):
  cost = {}
  for res in cost_info:
    if res in enum.Resource.values:
      cost[res] = int(cost_info[res])
    else:
      raise exception.ParseError('cost')
  return cost

def _parseResources(resources):
  if not isinstance(resources, list):
    raise exception.ParseError('resources', msg='Field must be a list.')
  return [tuple(res) if isinstance(res, list) else res for res in resources]

def _parseRelations(relations):
  return [_parseEnum(rel, enum.Relation, 'relations') for rel in relations]

def _parseWonders(wonders):
  output = []
  for wonder_info in wonders:
    output.append(_parseWonder(wonder_info))
  return output

def _parseWonder(wonder_info):
  name = str(wonder_info['name'])
  if not name:
    raise exception.ParseError('wonder.name')

  # TODO

  wonder = wonder_lib.Wonder(name=name, stages=None)
  return wonder
