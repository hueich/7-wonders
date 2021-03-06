#!/usr/bin/env python

import unittest

TEST_DIR = 'tests'
TEST_FILE_PATTERN = '*_test.py'

if __name__ == '__main__':
  suite = unittest.TestLoader().discover(TEST_DIR, pattern=TEST_FILE_PATTERN)
  results = unittest.TextTestRunner().run(suite)
  if not results.wasSuccessful():
    exit(1)
