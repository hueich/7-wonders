
import unittest

import bonus
import card
import constants
import enum
import exception
import loader
import wonder

class LoaderTest(unittest.TestCase):
  def testLoadOriginalAssets(self):
    with open('res/original.7wr') as fp:
      assets = loader.loadAssets(fp)
    self.assertIn(constants.CARDS_KEY, assets)
    self.assertGreater(len(assets[constants.CARDS_KEY]), 0)
    self.assertIn(constants.WONDERS_KEY, assets)
    self.assertGreater(len(assets[constants.WONDERS_KEY]), 0)

class ParseCardTest(unittest.TestCase):
  def testBasicResourceCard(self):
    json = {"type":"BASIC_RES", "name":"Boo", "age":"I", "min_players":[3], "cost":{}, "bonus":{"type":"RESOURCE", "resources":["WOOD"]}}
    expect = card.BasicResourceCard('Boo', enum.Age.I, 3, bonus.ResourceBonus([enum.Resource.WOOD]))
    cards = []
    loader._parseCard(json, cards)
    self.assertEqual(1, len(cards))
    self.assertEqual(expect, cards[0])

  def testAdvResourceCard(self):
    json = {"type":"ADV_RES", "name":"Doo", "age":"II", "min_players":[4], "cost":{"STONE":1}, "bonus":{"type":"RESOURCE", "resources":["PAPYRUS"]}}
    expect = card.AdvResourceCard('Doo', enum.Age.II, 4, bonus.ResourceBonus([enum.Resource.PAPYRUS]), {enum.Resource.STONE: 1})
    cards = []
    loader._parseCard(json, cards)
    self.assertEqual(1, len(cards))
    self.assertEqual(expect, cards[0])

  def testScienceCard(self):
    json = {"type":"SCIENCE", "name":"Sci fi", "age":"II", "min_players":[5], "cost":{}, "bonus":{"type":"SCIENCE", "science":"WHEEL"}}
    expect = card.ScienceCard('Sci fi', enum.Age.II, 5, bonus.ScienceBonus(enum.Science.WHEEL))
    cards = []
    loader._parseCard(json, cards)
    self.assertEqual(1, len(cards))
    self.assertEqual(expect, cards[0])

  def testMilitaryCard(self):
    json = {"type":"MILITARY", "name":"Mili", "age":"III", "min_players":[2], "cost":{}, "bonus":{"type":"MILITARY", "shields":3}}
    expect = card.MilitaryCard('Mili', enum.Age.III, 2, bonus.MilitaryBonus(3))
    cards = []
    loader._parseCard(json, cards)
    self.assertEqual(1, len(cards))
    self.assertEqual(expect, cards[0])

  def testCivilCard(self):
    json = {"type":"CIVIL", "name":"Civ", "age":"II", "min_players":[4], "cost":{"PAPYRUS":2}, "bonus":{"type":"POINT", "points":8}}
    expect = card.CivilCard('Civ', enum.Age.II, 4, bonus.PointBonus(8), {enum.Resource.PAPYRUS: 2})
    cards = []
    loader._parseCard(json, cards)
    self.assertEqual(1, len(cards))
    self.assertEqual(expect, cards[0])

  def testCommerceCard(self):
    json = {"type":"COMMERCE", "name":"Comm", "age":"I", "min_players":[3], "cost":{}, "bonus":{"type":"TRADING", "resources":["WOOD", "CLAY"], "relations":["LEFT"]}}
    expect = card.CommerceCard('Comm', enum.Age.I, 3, bonus.TradingBonus(resources=[enum.Resource.WOOD, enum.Resource.CLAY], relations=[enum.Relation.LEFT]))
    cards = []
    loader._parseCard(json, cards)
    self.assertEqual(1, len(cards))
    self.assertEqual(expect, cards[0])

  def testGuildCard(self):
    json = {"type":"GUILD", "name":"Guildy", "age":"III", "min_players":[5], "cost":{}, "bonus":{"type":"CARD_COUNT", "relations":["LEFT", "RIGHT"], "card_type":"CIVIL", "points_per_card":2, "coins_per_card":1}}
    expect = card.GuildCard('Guildy', enum.Age.III, 5, bonus.CardCountBonus(relations=[enum.Relation.LEFT, enum.Relation.RIGHT], card_type=card.CivilCard, points_per_card=2, coins_per_card=1))
    cards = []
    loader._parseCard(json, cards)
    self.assertEqual(1, len(cards))
    self.assertEqual(expect, cards[0])

  def testMultipleMinPlayers(self):
    json = {"type":"BASIC_RES", "name":"Boo", "age":"I", "min_players":[3, 5], "cost":{}, "bonus":{"type":"RESOURCE", "resources":["WOOD"]}}
    expect_0 = card.BasicResourceCard('Boo', enum.Age.I, 3, bonus.ResourceBonus([enum.Resource.WOOD]))
    expect_1 = card.BasicResourceCard('Boo', enum.Age.I, 5, bonus.ResourceBonus([enum.Resource.WOOD]))
    cards = []
    loader._parseCard(json, cards)
    self.assertEqual(2, len(cards))
    self.assertEqual(expect_0, cards[0])
    self.assertEqual(expect_1, cards[1])

  def testSingleParent(self):
    json = {"type":"CIVIL", "name":"Boo", "age":"I", "min_players":[3], "cost":{}, "bonus":{"type":"POINT", "points":2}, "parents":["abc"]}
    expect = card.CivilCard('Boo', enum.Age.I, 3, bonus.PointBonus(2), parents=['abc'])
    cards = []
    loader._parseCard(json, cards)
    self.assertEqual(1, len(cards))
    self.assertEqual(expect, cards[0])

  def testMultipleParents(self):
    json = {"type":"CIVIL", "name":"Boo", "age":"I", "min_players":[3], "cost":{}, "bonus":{"type":"POINT", "points":2}, "parents":["abc", "def"]}
    expect = card.CivilCard('Boo', enum.Age.I, 3, bonus.PointBonus(2), parents=['abc', 'def'])
    cards = []
    loader._parseCard(json, cards)
    self.assertEqual(1, len(cards))
    self.assertEqual(expect, cards[0])

  def testMultipleChildren(self):
    json = {"type":"CIVIL", "name":"Boo", "age":"I", "min_players":[3], "cost":{}, "bonus":{"type":"POINT", "points":2}, "children":["abc", "def"]}
    expect = card.CivilCard('Boo', enum.Age.I, 3, bonus.PointBonus(2), children=['abc', 'def'])
    cards = []
    loader._parseCard(json, cards)
    self.assertEqual(1, len(cards))
    self.assertEqual(expect, cards[0])

  def testMultipleParentsAndChildren(self):
    json = {"type":"CIVIL", "name":"Boo", "age":"I", "min_players":[3], "cost":{}, "bonus":{"type":"POINT", "points":2}, "parents":["abc", "def"], "children":["123", "456"]}
    expect = card.CivilCard('Boo', enum.Age.I, 3, bonus.PointBonus(2), parents=['abc', 'def'], children=['123', '456'])
    cards = []
    loader._parseCard(json, cards)
    self.assertEqual(1, len(cards))
    self.assertEqual(expect, cards[0])


class ParseBonusTest(unittest.TestCase):
  def testCountCardsSimple(self):
    json = {"type":"CARD_COUNT", "relations":["RIGHT", "LEFT"], "card_type":"BASIC_RES"}
    expect = bonus.CardCountBonus(relations=[enum.Relation.RIGHT, enum.Relation.LEFT], card_type=card.BasicResourceCard)
    actual = loader._parseBonus(json)
    self.assertEqual(expect, actual)

  def testCountCardsAllParams(self):
    json = {"type":"CARD_COUNT", "relations":["SELF"], "card_type":"GUILD", "points_per_card":2, "coins_per_card":3}
    expect = bonus.CardCountBonus(relations=[enum.Relation.SELF], card_type=card.GuildCard, points_per_card=2, coins_per_card=3)
    actual = loader._parseBonus(json)
    self.assertEqual(expect, actual)

  def testCountWonderAllParams(self):
    json = {"type":"WONDER_COUNT", "relations":["SELF"], "points_per_stage":1, "coins_per_stage":2}
    expect = bonus.WonderCountBonus(relations=[enum.Relation.SELF], points_per_stage=1, coins_per_stage=2)
    actual = loader._parseBonus(json)
    self.assertEqual(expect, actual)

  def testCountDefeat(self):
    json = {"type":"DEFEAT_COUNT", "relations":["LEFT", "SELF", "RIGHT"], "points_per_defeat":4}
    expect = bonus.DefeatCountBonus(relations=[enum.Relation.LEFT, enum.Relation.SELF, enum.Relation.RIGHT], points_per_defeat=4)
    actual = loader._parseBonus(json)
    self.assertEqual(expect, actual)

  def testParseCoins(self):
    json = {"type":"COIN", "coins":3}
    expect = bonus.CoinBonus(coins=3)
    actual = loader._parseBonus(json)
    self.assertEqual(expect, actual)


class ParseWonderTest(unittest.TestCase):
  def testSimpleWonder(self):
    json = {"name":"Foo Wonder of Bar City", "resource":"CLAY", "stages":[{"cost":{"CLAY":4, "GLASS":1}, "bonus":{"type":"POINT", "points":7}}]}
    expect = wonder.Wonder(name='Foo Wonder of Bar City', resource=enum.Resource.CLAY, stages=[wonder.Stage({enum.Resource.CLAY: 4, enum.Resource.GLASS: 1}, bonus.PointBonus(7))])
    actual = loader._parseWonder(json)
    self.assertEqual(expect, actual)

  def testParseStageSimple(self):
    json = {"cost":{"PAPYRUS":2}, "bonus":{"type":"POINT", "points":7}}
    expect = wonder.Stage({enum.Resource.PAPYRUS: 2}, bonus.PointBonus(7))
    actual = loader._parseStage(json)
    self.assertEqual(expect, actual)

class UtilsTest(unittest.TestCase):
  def testGetIntOrNoneHasKey(self):
    dct = {'abc': 123}
    self.assertEqual(123, loader._getIntOrNone(dct, 'abc'))

  def testGetIntOrNoneHasNoKey(self):
    dct = {'abc': 123}
    self.assertIsNone(loader._getIntOrNone(dct, 'def'))

  def testParseEnum(self):
    enum_type = enum.Resource
    value = 'ORE'
    self.assertEqual(value, loader._parseEnum(value, enum_type))

  def testParseEnum(self):
    enum_type = enum.Resource
    value = 'blab'
    self.assertRaises(exception.ParseError, loader._parseEnum, value, enum_type)

  def testParseCost(self):
    info = {'cost': {'WOOD': 2, 'PAPYRUS': 1, 'COIN': 3}}
    self.assertEqual(info['cost'], loader._parseCost(info))

  def testParseCostInvalidKey(self):
    info = {'cost': {'blah': 2}}
    self.assertRaises(exception.ParseError, loader._parseCost, info)

  def testParseCostNonExistent(self):
    info = {}
    self.assertEqual({}, loader._parseCost(info))

  def testParseResources(self):
    resources = ['STONE', 'CLAY']
    self.assertEqual(resources, loader._parseResources(resources))

  def testParseResourcesMultiple(self):
    resources = ['CLAY', 'CLAY']
    self.assertEqual(resources, loader._parseResources(resources))

  def testParseResourcesNotList(self):
    resources = 'TEXTILE'
    self.assertRaises(exception.ParseError, loader._parseResources, resources)

  def testParseResourcesChoice(self):
    resources = ['ORE', ['GLASS', 'TEXTILE', 'PAPYRUS']]
    expect = ['ORE', ('GLASS', 'TEXTILE', 'PAPYRUS')]
    self.assertEqual(expect, loader._parseResources(resources))
