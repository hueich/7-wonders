
def enum(*keys):
    enums = dict(zip(keys, keys), values=keys)
    return type('Enum', (object,), enums)

Age = enum(
  'I',
  'II',
  'III',
)

Resource = enum(
  # Basic Resources
  'WOOD',
  'STONE',
  'ORE',
  'CLAY',
  # Advanced Resources
  'PAPYRUS',
  'TEXTILE',
  'GLASS',
  # Other
  'COIN',
)

Science = enum(
  'WHEEL',
  'COMPASS',
  'TABLET',
)

Relation = enum(
  'SELF',
  'LEFT',
  'RIGHT',
)

Direction = enum(
  'CLOCKWISE',
  'COUNTERCLOCKWISE',
)

Action = enum(
  'BUILD',
  'WONDER',
  'EXCHANGE',
)

CardType = enum(
  'BASIC_RES',  # Brown
  'ADV_RES',    # Gray
  'SCIENCE',    # Green
  'MILITARY',   # Red
  'CIVIL',      # Blue
  'COMMERCE',   # Yellow
  'GUILD',      # Purple
)

BonusType = enum(
  'POINT',
  'RESOURCE',
  'SCIENCE',
  'MILITARY',
  'TRADING',
  'CARD_COUNT',
  'WONDER_COUNT',
  'DEFEAT_COUNT',
)
