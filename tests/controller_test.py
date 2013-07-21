
import mox
import unittest

import controller

class GameTest(unittest.TestCase):
  def setUp(self):
    self.mox = mox.Mox()

  def tearDown(self):
    self.mox.UnsetStubs()

  def testCreateGame(self):
    self.mox.StubOutWithMock(controller.Game, '_loadAssets')
    controller.Game._loadAssets(None)

    self.mox.ReplayAll()

    game = controller.Game()
    self.assertIsNotNone(game)

    self.mox.VerifyAll()
