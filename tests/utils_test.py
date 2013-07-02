
import unittest

import card
import enum
import utils

class UtilsTest(unittest.TestCase):
  def testGetCardsOfType(self):
    input_cards = [card.ResourceCard('A', enum.Age.I, [enum.Resource.WOOD]), card.CivilCard('B', enum.Age.II, 3)]
    output_cards = utils.getCardsOfType(input_cards, card.CivilCard)
    self.assertEqual(1, len(output_cards))
    self.assertEqual(output_cards[0], input_cards[1])

  def testGetCardsOfTypeNoMatch(self):
    input_cards = [card.ResourceCard('A', enum.Age.I, [enum.Resource.WOOD]), card.CivilCard('B', enum.Age.II, 3)]
    output_cards = utils.getCardsOfType(input_cards, card.ScienceCard)
    self.assertEqual([], output_cards)
