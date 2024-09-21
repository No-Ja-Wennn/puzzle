import copy

class State:
  def __init__(self, data = None, par = None,
              g = 0, h = 0, op = None):
    self.data = data
    self.par = par
    self.g = g
    self.h = h
    self.op = op
  def clone(self):
    sn = copy.deepcopy(self)
    return sn
  def Print(self):
    sz = 3
    for i in range(sz):
      for j in range(sz):
        print(self.data[i * sz + j], end = ' ')
      print()
    print()

  def Key(self):
    if self.data == None:
      return None
    res = ''
    for x in self.data:
      res += (str) (x)
    return res
  def __lt__(self, other):
    if other == None:
      return False
    return self.g + self.h < other.g + other.h
  
  def __eq__(self, other):
    if other == None:
      return False
    return self.Key() == other.Key()
