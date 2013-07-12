
import unittest

import bonus
import card
import enum
import loader

class LoaderTest(unittest.TestCase):
  pass

class ParseCardTest(unittest.TestCase):
  def testBasicResourceCard(self):
    json = {"type":"BASIC_RES", "name":"Boo", "age":"I", "min_players":[3], "cost":{}, "bonus":{"type":"RESOURCE", "resources":["WOOD"]}}
    cards = []
    loader._parseCard(json, cards)
    self.assertEqual(1, len(cards))
    self.assertEqual(card.BasicResourceCard('Boo', enum.Age.I, 3, bonus.ResourceBonus([enum.Resource.WOOD])), cards[0])

  def testAdvResourceCard(self):
    json = {"type":"ADV_RES", "name":"Doo", "age":"II", "min_players":[4], "cost":{"STONE":1}, "bonus":{"type":"RESOURCE", "resources":["PAPYRUS"]}}
    cards = []
    loader._parseCard(json, cards)
    self.assertEqual(1, len(cards))
    self.assertEqual(card.AdvResourceCard('Doo', enum.Age.II, 4, bonus.ResourceBonus([enum.Resource.PAPYRUS]), {enum.Resource.STONE: 1}), cards[0])

  def testScienceCard(self):
    json = {"type":"SCIENCE", "name":"Sci fi", "age":"II", "min_players":[5], "cost":{}, "bonus":{"type":"SCIENCE", "science":"WHEEL"}}
    cards = []
    loader._parseCard(json, cards)
    self.assertEqual(1, len(cards))
    self.assertEqual(card.ScienceCard('Sci fi', enum.Age.II, 5, bonus.ScienceBonus(enum.Science.WHEEL)), cards[0])

  def testMilitaryCard(self):
    json = {"type":"MILITARY", "name":"Mili", "age":"III", "min_players":[2], "cost":{}, "bonus":{"type":"MILITARY", "shields":3}}
    cards = []
    loader._parseCard(json, cards)
    self.assertEqual(1, len(cards))
    self.assertEqual(card.MilitaryCard('Mili', enum.Age.III, 2, bonus.MilitaryBonus(3)), cards[0])

  def testCivilCard(self):
    json = {"type":"CIVIL", "name":"Civ", "age":"II", "min_players":[4], "cost":{"PAPYRUS":2}, "bonus":{"type":"POINT", "points":8}}
    cards = []
    loader._parseCard(json, cards)
    self.assertEqual(1, len(cards))
    self.assertEqual(card.CivilCard('Civ', enum.Age.II, 4, bonus.PointBonus(8), {enum.Resource.PAPYRUS: 2}), cards[0])

  def testCommerceCard(self):
    json = {"type":"COMMERCE", "name":"Comm", "age":"I", "min_players":[3], "cost":{}, "bonus":{"type":"TRADING", "resources":["WOOD", "CLAY"], "relations":["LEFT"]}}
    cards = []
    loader._parseCard(json, cards)
    self.assertEqual(1, len(cards))
    self.assertEqual(card.CommerceCard('Comm', enum.Age.I, 3, bonus.TradingBonus(resources=[enum.Resource.WOOD, enum.Resource.CLAY], relations=[enum.Relation.LEFT])), cards[0])

  def testGuildCard(self):
    json = {"type":"GUILD", "name":"Guildy", "age":"III", "min_players":[5], "cost":{}, "bonus":{"type":"CARD_COUNT", "relations":["LEFT", "RIGHT"], "card_type":"CIVIL", "points_per_card":2, "coins_per_card":1}}
    cards = []
    loader._parseCard(json, cards)
    self.assertEqual(1, len(cards))
    self.assertEqual(card.GuildCard('Guildy', enum.Age.III, 5, bonus.CardCountBonus(relations=[enum.Relation.LEFT, enum.Relation.RIGHT], card_type=card.CivilCard, points_per_card=2, coins_per_card=1)), cards[0])

  def testMultipleMinPlayers(self):
    json = {"type":"BASIC_RES", "name":"Boo", "age":"I", "min_players":[3, 5], "cost":{}, "bonus":{"type":"RESOURCE", "resources":["WOOD"]}}
    cards = []
    loader._parseCard(json, cards)
    self.assertEqual(2, len(cards))
    self.assertEqual(card.BasicResourceCard('Boo', enum.Age.I, 3, bonus.ResourceBonus([enum.Resource.WOOD])), cards[0])
    self.assertEqual(card.BasicResourceCard('Boo', enum.Age.I, 5, bonus.ResourceBonus([enum.Resource.WOOD])), cards[1])

  def testSingleParent(self):
    json = {"type":"CIVIL", "name":"Boo", "age":"I", "min_players":[3], "cost":{}, "bonus":{"type":"POINT", "points":2}, "parents":["abc"]}
    cards = []
    loader._parseCard(json, cards)
    self.assertEqual(1, len(cards))
    self.assertEqual(card.CivilCard('Boo', enum.Age.I, 3, bonus.PointBonus(2), parents=['abc']), cards[0])

  def testMultipleParents(self):
    json = {"type":"CIVIL", "name":"Boo", "age":"I", "min_players":[3], "cost":{}, "bonus":{"type":"POINT", "points":2}, "parents":["abc", "def"]}
    cards = []
    loader._parseCard(json, cards)
    self.assertEqual(1, len(cards))
    self.assertEqual(card.CivilCard('Boo', enum.Age.I, 3, bonus.PointBonus(2), parents=['abc', 'def']), cards[0])

  def testMultipleChildren(self):
    json = {"type":"CIVIL", "name":"Boo", "age":"I", "min_players":[3], "cost":{}, "bonus":{"type":"POINT", "points":2}, "children":["abc", "def"]}
    cards = []
    loader._parseCard(json, cards)
    self.assertEqual(1, len(cards))
    self.assertEqual(card.CivilCard('Boo', enum.Age.I, 3, bonus.PointBonus(2), children=['abc', 'def']), cards[0])

  def testMultipleParentsAndChildren(self):
    json = {"type":"CIVIL", "name":"Boo", "age":"I", "min_players":[3], "cost":{}, "bonus":{"type":"POINT", "points":2}, "parents":["abc", "def"], "children":["123", "456"]}
    cards = []
    loader._parseCard(json, cards)
    self.assertEqual(1, len(cards))
    self.assertEqual(card.CivilCard('Boo', enum.Age.I, 3, bonus.PointBonus(2), parents=['abc', 'def'], children=['123', '456']), cards[0])


class ParseBonusTest(unittest.TestCase):
  def testCountCardsSimple(self):
    json = {"type":"CARD_COUNT", "relations":["RIGHT", "LEFT"], "card_type":"BASIC_RES"}
    actual = loader._parseBonus(json)
    self.assertEqual(bonus.CardCountBonus(relations=[enum.Relation.RIGHT, enum.Relation.LEFT], card_type=card.BasicResourceCard), actual)

  def testCountCardsAllParams(self):
    json = {"type":"CARD_COUNT", "relations":["SELF"], "card_type":"GUILD", "points_per_card":2, "coins_per_card":3}
    actual = loader._parseBonus(json)
    self.assertEqual(bonus.CardCountBonus(relations=[enum.Relation.SELF], card_type=card.GuildCard, points_per_card=2, coins_per_card=3), actual)

  def testCountWonderAllParams(self):
    json = {"type":"WONDER_COUNT", "relations":["SELF"], "points_per_stage":1, "coins_per_stage":2}
    actual = loader._parseBonus(json)
    self.assertEqual(bonus.WonderCountBonus(relations=[enum.Relation.SELF], points_per_stage=1, coins_per_stage=2), actual)

  def testCountDefeat(self):
    json = {"type":"DEFEAT_COUNT", "relations":["LEFT", "SELF", "RIGHT"], "points_per_defeat":4}
    actual = loader._parseBonus(json)
    self.assertEqual(bonus.DefeatCountBonus(relations=[enum.Relation.LEFT, enum.Relation.SELF, enum.Relation.RIGHT], points_per_defeat=4), actual)


