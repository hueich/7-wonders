
import itertools
import mox
import unittest

import card as card_lib
import constants
import controller
import enum
import utils

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
      all_cards.append(card_lib.GuildCard('Card_%s' % i, enum.Age.III, -1, None))
    self.game._all_cards = all_cards
    self.game._players = range(num_players)

    self.game._selectGuildCards()
    guild_cards = self.game._guild_cards

    self.assertEqual(expected_num_cards, len(guild_cards))
    for c in guild_cards:
      self.assertIn(c, all_cards)

  def testPruneCardsByNumPlayers(self):
    all_cards = []
    for i in xrange(3, 6):
      all_cards.append(card_lib.BasicResourceCard('Card_%s' % i, enum.Age.I, i, None))
    self.game._all_cards = all_cards
    self.game._players = range(4)

    pruned_cards = self.game._pruneCardsByNumPlayers()

    self.assertEqual(all_cards[:2], pruned_cards)

  # def testPartitionCards(self):
  #   input_cards = [
  #     card_lib.BasicResourceCard('Card_1', enum.Age.I, 3, None),
  #     card_lib.BasicResourceCard('Card_2', enum.Age.II, 3, None),
  #     card_lib.BasicResourceCard('Card_3', enum.Age.III, 3, None)
  #   ]

  #   self.game._partitionCardsIntoAges(input_cards)

  #   self.assertEqual(input_cards[:1], self.game._age1_cards)
  #   self.assertEqual(input_cards[1:2], self.game._age2_cards)
  #   self.assertEqual(input_cards[2:], self.game._age3_cards)

  def testShuffleAndDeal(self):
    num_cards = 15
    num_stacks = 3
    stack_size = num_cards / num_stacks
    cards = range(num_cards)
    stacks = self.game._shuffleAndDeal(cards, num_stacks)
    self.assertEqual(num_stacks, len(stacks))
    for stack in stacks:
      self.assertEqual(stack_size, len(stack))

  def testResolveMilitaryConflicts(self):
    age = enum.Age.II
    win_pts = constants.MILITARY_WIN_POINTS_BY_AGE[age]
    players = range(5)
    self.game._current_age = age
    self.game._players = players
    self.mox.StubOutWithMock(utils, 'resolveCombat')
    for p1, p2 in itertools.combinations(self.game._players, 2):
      utils.resolveCombat(p1, p2, win_pts)

    self.mox.ReplayAll()
    self.game.resolveMilitaryConflicts()
    self.mox.VerifyAll()
