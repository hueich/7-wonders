import json

import card
import constants
import wonder

def loadAssets(fp):
  output = json.load(fp)
  assets = {
    constants.CARDS_KEY: _parseCards(output[constants.CARDS_KEY]),
    constants.WONDERS_KEY: _parseWonders(output[constants.WONDERS_KEY])
  }
  return assets

def _parseCards(cards):
  output = []
  for card_info in cards:
    pass
  return output

def _parseWonders(wonders):
  output = []
  for wonder_info in wonders:
    pass
  return output
