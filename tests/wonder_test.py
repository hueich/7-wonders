
import unittest

import bonus
import enum
import wonder as wonder_lib

class WonderTest(unittest.TestCase):
  def testCreateWonder(self):
    wonder = wonder_lib.Wonder('Boogie', enum.Resource.PAPYRUS, [])
    self.assertIsNotNone(wonder)

class StageTest(unittest.TestCase):
  def testCreateStage(self):
    stage = wonder_lib.Stage({enum.Resource.CLAY: 2}, bonus.PointBonus(3))
    self.assertIsNotNone(stage)
