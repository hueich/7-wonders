
def getCardsOfType(cards, card_type):
  return [c for c in cards if isinstance(c, card_type)]
