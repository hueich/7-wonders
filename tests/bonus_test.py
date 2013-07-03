
import unittest

import bonus as bonus_lib
import card
import enum
import player as player_lib
import wonder as wonder_lib

class BonusTest(unittest.TestCase):
  def testCardBonusCounting(self):
    player = player_lib.Player(name='A', wonder=None)
    player.cards = [card.MilitaryCard(None, None, None), card.ScienceCard(None, None, None)]
    bonus = bonus_lib.CardBonus([enum.Relation.SELF], card.ScienceCard, coins_per_card=3)
    self.assertEqual(1, bonus.getCount(player))

  def testWonderBonusCounting(self):
    wonder = wonder_lib.Wonder('Boo', ['1', '2', '3'])
    player = player_lib.Player(name='A', wonder=wonder)
    player.wonder_stage = 2
    bonus = bonus_lib.WonderBonus([enum.Relation.SELF], points_per_stage=3)
    self.assertEqual(2, bonus.getCount(player))
