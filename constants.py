
import enum

PLAYER_STARTING_COINS = 3
"""Number of coins a player starts with."""

CARD_EXCHANGE_RATE = 3
"""Number of coins received for exchainging a card."""

INITIAL_TRADING_RATE = 2
"""Cost per resource traded without any modifiers."""

COMMERCE_TRADING_RATE = 1
"""Cost per resource traded through commerce."""

# Dict keys
CARDS_KEY = 'cards'
WONDERS_KEY = 'wonders'

MILITARY_WIN_POINTS_BY_AGE = {
  enum.Age.I: 1,
  enum.Age.II: 3,
  enum.Age.III: 5
}
