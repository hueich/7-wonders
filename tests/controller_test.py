
import mox
import unittest

import card as card_lib
import controller
import enum

class GameTest(unittest.TestCase):
  def setUp(self):
    self.mox = mox.Mox()

    self.game = controller.Game()

  def tearDown(self):
    self.mox.UnsetStubs()

  def testCreateGame(self):
    self.assertIsNotNone(self.game)

  def testSelectGuildCards(self):
    num_players = 3
    expected_num_cards = num_players + 2
    all_cards = []
    for i in xrange(6):
      all_cards.append(card_lib.GuildCard('Card_%s' % i, enum.Age.III, 0, None))
    self.game._all_cards = all_cards
    self.game._players = range(num_players)

    self.game._selectGuildCards()

    self.assertEqual(expected_num_cards, len(self.game._age3_cards))
    for c in self.game._age3_cards:
      self.assertIn(c, all_cards)
