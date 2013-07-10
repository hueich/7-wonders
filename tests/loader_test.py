
import unittest

import bonus
import card
import enum
import loader

class LoaderTest(unittest.TestCase):
  pass

class ParseCardTest(unittest.TestCase):
  def testBasicResourceCard(self):
    json = {"type":"BASIC_RES", "name":"Boo", "age":"I", "min_players":[3], "cost":[], "bonus":{"type":"RESOURCE", "resources":["WOOD"]}}
    cards = []
    loader._parseCard(json, cards)
    self.assertEqual(1, len(cards))
    self.assertEqual(card.BasicResourceCard('Boo', enum.Age.I, 3, bonus.ResourceBonus([enum.Resource.WOOD])), cards[0])

  def testMultipleMinPlayers(self):
    json = {"type":"BASIC_RES", "name":"Boo", "age":"I", "min_players":[3, 5], "cost":[], "bonus":{"type":"RESOURCE", "resources":["WOOD"]}}
    cards = []
    loader._parseCard(json, cards)
    self.assertEqual(2, len(cards))
    self.assertEqual(card.BasicResourceCard('Boo', enum.Age.I, 3, bonus.ResourceBonus([enum.Resource.WOOD])), cards[0])
    self.assertEqual(card.BasicResourceCard('Boo', enum.Age.I, 5, bonus.ResourceBonus([enum.Resource.WOOD])), cards[1])
