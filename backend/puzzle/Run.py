from algorithm import *
from operator2 import Operator
from queue import PriorityQueue
from random import randint
def RUN(S, G):
  Open = PriorityQueue()
  Close = PriorityQueue()
  S.g = 0
  S.h = Hx(S, G)
  Open.put(S)
  while True:
    if Open.empty() == True:
      print('tim kiem that bai')
      return
    O = Open.get()
    Close.put(O)
    if Equal(O, G):
      print ('cac buoc giai:')
      Path(O)
      return
    #tat ca cac trang thai con
    for i in range(4):
      op = Operator(i)
      child = op.Move(O)
      if child == None:
        continue
      ok1 = checkInPrio(Open, child)
      ok2 = checkInPrio(Close, child)
      if not ok1 and not ok2:
        child.par = O
        child.op = op
        child.g = O.g + 1
        child.h = Hx(child, G)
        Open.put(child)

G = State()
sz = 3
G.data = [1, 2, 3, 4, 5 , 6, 7, 8, 0]
S = G.clone()
for i in range(20):
  op = Operator(randint(0, 3))
  tmp = op.Move(S)
  if tmp != None:
    S = tmp

S.Print()
G.Print()