import json

import bonus as bonus_lib
import card as card_lib
import constants
import enum
import exception
import wonder

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
    pass
  return output

def _parseCard(card_info, cards_list):
  # TODO
  for min_players in [int(c) for c in card_info['min_players']]:
    card_type = card_info['type'] if card_info['type'] in enum.CardType.values else None
    if not card_type:
      raise exception.ParseError('card.type')

    name = str(card_info['name'])
    if not name:
      raise exception.ParseError('card.type')

    age = card_info['age'] if card_info['age'] in enum.Age.values else None
    if not age:
      raise exception.ParseError('card.age')

    bonus = _parseBonus(card_info['bonus'])

    cost = _parseCost(card_info['cost'])

    # TODO
    parents = None
    children = None

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

    card = card_class(name, age, min_players, bonus, cost, parents, children)
    cards_list.append(card)


def _parseBonus(bonus_info):
  bonus_type = bonus_info['type'] if bonus_info['type'] in enum.BonusType.values else None
  bonus = None
  if bonus_type == enum.BonusType.POINT:
    points = int(bonus_info['points'])
    bonus = bonus_lib.PointBonus(points)
  elif bonus_type == enum.BonusType.RESOURCE:
    if not isinstance(bonus_info['resources'], list):
      raise exception.ParseError('bonus.resources', msg='Field must be a list.')
    resources = [tuple(res) if isinstance(res, list) else res for res in bonus_info['resources']]
    bonus = bonus_lib.ResourceBonus(resources)
  elif bonus_type == enum.BonusType.SCIENCE:
    science = bonus_info['science'] if bonus_info['science'] in enum.Science.values else None
    if not science:
      raise exception.ParseError('bonus.science')
    bonus = bonus_lib.ScienceBonus(science)
  elif bonus_type == enum.BonusType.MILITARY:
    shields = int(bonus_info['shields'])
    bonus = bonus_lib.MilitaryBonus(shields)
  # TODO
  else:
    raise exception.ParseError('bonus.type')
  return bonus

def _parseCost(cost_info):
  cost = {}
  for res in cost_info:
    if res in enum.Resource.values:
      cost[res] = int(cost_info[res])
    else:
      raise exception.ParseError('cost')
  return cost

def _parseWonders(wonders):
  output = []
  for wonder_info in wonders:
    pass
  return output
