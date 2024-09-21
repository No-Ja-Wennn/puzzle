from state import State
# kiem tra xem co thuoc mang hay khong
def checkInPrio(Open, tmp):
  if tmp == None:
    return False
  return (tmp in Open.queue)

# kiem tra xem co bang nhau hay khong
def Equal(O, G):
  if O == None:
    return False
  return O == G

# kiem tra xem co bang Null hay khong
def Path(O):
  if O.par != None:
    Path(O.par)
    # print(O.op.i)
  O.Print()

# ham danh gia A*
def Hx(S, G):
  sz = 3
  res = 0
  for i in range(sz):
    for j in range(sz):
      if S.data[i * sz + j] != G.data[i * sz + j]:
        res += 1
  return res
