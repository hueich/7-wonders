
class Wonder(object):
  def __init__(self, name, stages):
    self.name = name
    self.stages = stages

  def __eq__(self, other):
    return self.__dict__ == other.__dict__

  def __str__(self):
    return self.__class__.__name__ + ': ' + str(self.__dict__)

  def __repr__(self):
    return '<' + str(self) + '>'

class Stage(object):
  def __init__(self, cost):
    self.cost = cost
