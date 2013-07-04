
import unittest

import enum

class EnumTest(unittest.TestCase):
  def setUp(self):
    self.myEnum = enum.enum('A', 'B', 'C')

  def testCreateEnum(self):
    self.assertEqual('A', self.myEnum.A)
    self.assertEqual('B', self.myEnum.B)
    self.assertEqual('C', self.myEnum.C)

  def testEnumValues(self):
    self.assertEqual(('A', 'B', 'C'), self.myEnum.values)

  def testNoEnumValue(self):
    with self.assertRaises(AttributeError):
      self.myEnum.NOT_THERE
