
import unittest

import card
import enum
import utils

class UtilsTest(unittest.TestCase):
  def testGetCardsOfType(self):
    input_cards = self._makeTestCards()
    output_cards = utils.getCardsOfType(input_cards, card.CivilCard)
    self.assertEqual(1, len(output_cards))
    self.assertEqual(output_cards[0], input_cards[1])

  def testGetCardsOfTypeNoMatch(self):
    input_cards = self._makeTestCards()
    output_cards = utils.getCardsOfType(input_cards, card.ScienceCard)
    self.assertEqual([], output_cards)

  def _makeTestCards(self):
    return [
      card.BasicResourceCard('A', enum.Age.I, 6, [enum.Resource.WOOD]),
      card.CivilCard('B', enum.Age.II, 5, 3),
      card.MilitaryCard('C', enum.Age.III, 4, 2)
    ]
