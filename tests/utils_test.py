
import mox
import unittest

import card
import enum
import player as player_lib
import utils

class UtilsTest(unittest.TestCase):
  def setUp(self):
    self.mox = mox.Mox()

  def tearDown(self):
    self.mox.UnsetStubs()

  def testGetCardsOfType(self):
    input_cards = self._makeTestCards()
    output_cards = utils.getCardsOfType(input_cards, card.CivilCard)
    self.assertEqual(output_cards, input_cards[1:2])

  def testGetCardsOfTypeNoMatch(self):
    input_cards = self._makeTestCards()
    output_cards = utils.getCardsOfType(input_cards, card.ScienceCard)
    self.assertEqual([], output_cards)

  def testGetCardsOfAge(self):
    input_cards = self._makeTestCards()
    output_cards = utils.getCardsOfAge(input_cards, enum.Age.III)
    self.assertEqual(output_cards, input_cards[2:3])

  def _makeTestCards(self):
    return [
      card.BasicResourceCard('A', enum.Age.I, 6, [enum.Resource.WOOD]),
      card.CivilCard('B', enum.Age.II, 5, 3),
      card.MilitaryCard('C', enum.Age.III, 4, 2)
    ]

def testShuffleAndDeal(self):
  num_cards = 15
  num_stacks = 3
  stack_size = num_cards / num_stacks
  cards = range(num_cards)
  stacks = shuffleAndDeal(cards, num_stacks)
  self.assertEqual(num_stacks, len(stacks))
  for stack in stacks:
    self.assertEqual(stack_size, len(stack))

  def testResolveCombatP1Win(self):
    win_pts = 4
    p1_shields = 3
    p2_shields = 2
    p1 = player_lib.Player('A')
    p2 = player_lib.Player('B')

    self.mox.StubOutWithMock(utils, 'getNumShields')
    utils.getNumShields(p1).AndReturn(p1_shields)
    utils.getNumShields(p2).AndReturn(p2_shields)

    self.mox.ReplayAll()
    utils.resolveCombat(p1, p2, win_pts)
    self.mox.VerifyAll()

    self.assertEqual(win_pts, p1.wins)
    self.assertEqual(0, p1.losses)
    self.assertEqual(0, p2.wins)
    self.assertEqual(1, p2.losses)

  def testResolveCombatP2Win(self):
    win_pts = 3
    p1_shields = 3
    p2_shields = 5
    p1 = player_lib.Player('A')
    p2 = player_lib.Player('B')

    self.mox.StubOutWithMock(utils, 'getNumShields')
    utils.getNumShields(p1).AndReturn(p1_shields)
    utils.getNumShields(p2).AndReturn(p2_shields)

    self.mox.ReplayAll()
    utils.resolveCombat(p1, p2, win_pts)
    self.mox.VerifyAll()

    self.assertEqual(0, p1.wins)
    self.assertEqual(1, p1.losses)
    self.assertEqual(win_pts, p2.wins)
    self.assertEqual(0, p2.losses)

  def testResolveCombatTie(self):
    win_pts = 5
    p1_shields = 4
    p2_shields = 4
    p1 = player_lib.Player('A')
    p2 = player_lib.Player('B')

    self.mox.StubOutWithMock(utils, 'getNumShields')
    utils.getNumShields(p1).AndReturn(p1_shields)
    utils.getNumShields(p2).AndReturn(p2_shields)

    self.mox.ReplayAll()
    utils.resolveCombat(p1, p2, win_pts)
    self.mox.VerifyAll()

    self.assertEqual(0, p1.wins)
    self.assertEqual(0, p1.losses)
    self.assertEqual(0, p2.wins)
    self.assertEqual(0, p2.losses)
