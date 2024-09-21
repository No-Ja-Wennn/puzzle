from state import State
class Operator:
  def __init__(self, i):
    self.i = i
  # het def init

  def checkStateNull(self, s):
    return s.data == None
  # het def checkStateNull

  # ham findPos tim ra vi tri Nul
  def findPos(self, s):
    sz = 3
    for i in range(sz):
      for j in range(sz):
        if s.data[i * sz + j] == 0:
          return i, j
    return None
  # het def findPos

  # ham swap de thay doi vi tri x, y
  def Swap(self, s, x, y, i):
    sz = 3
    sn = s.clone()
    x_new = x
    y_new = y
    # up, down
    if i == 0:
      x_new = x + 1
      y_new = y
    if i == 1:
      x_new = x - 1
      y_new = y
    # lelf, right
    if i == 2:
      x_new = x
      y_new = y + 1
    if i == 3:
      x_new = x
      y_new = y - 1
    sn.data[x * sz + y] = sn.data[x_new * sz + y_new]
    sn.data[x_new * sz + y_new] = 0
    return sn
  # het def swap

  def Up(self, s):
    if self.checkStateNull(s) == True:
      return None
    x, y = self.findPos(s)
    if x == 2:
      return None
    return self.Swap(s, x, y, self.i)
  # het def up

  def Down(self, s):
    if self.checkStateNull(s) == True:
      return None
    x, y = self.findPos(s)
    if x == 0:
      return None
    return self.Swap(s, x, y, self.i)
  # het def down

  def Left(self, s):
    if self.checkStateNull(s) == True:
      return None
    x, y = self.findPos(s)
    if y == 2:
      return None
    return self.Swap(s, x, y, self.i)
  # het def left

  def Right(self, s):
    if self.checkStateNull(s) == True:
      return None
    x, y = self.findPos(s)
    if y == 0:
      return None
    return self.Swap(s, x, y, self.i)
  # het def right



  def Move(self, s):
    if self.i == 0:
      return self.Up(s)
    if self.i == 1:
      return self.Down(s)
    if self.i == 2:
      return self.Left(s)
    if self.i == 3:
      return self.Right(s)
    return None
  # het def move