
class Wonder(object):
  def __init__(self, name, stages, resource):
    """
    Args:
      name: Name of the wonder.
      stages: List of stages, in order.
      resource: The resource that the wonder provides.
    """
    self.name = name
    self.stages = stages
    self.resource = resource

  def __eq__(self, other):
    return self.__dict__ == other.__dict__

  def __str__(self):
    return self.__class__.__name__ + ': ' + str(self.__dict__)

  def __repr__(self):
    return '<' + str(self) + '>'


  def __eq__(self, other):
    return self.__dict__ == other.__dict__

  def __str__(self):
    return self.__class__.__name__ + ': ' + str(self.__dict__)

  def __repr__(self):
    return '<' + str(self) + '>'

class Stage(object):
  def __init__(self, cost, bonus):
    """
    Args:
      cost: Cost of building the stage. A dict of resource type to amount, e.g. {'WOOD':1, 'COIN':3}
      bonus: The bonus this stage provides.
    """
    self.cost = cost
    self.bonus = bonus
