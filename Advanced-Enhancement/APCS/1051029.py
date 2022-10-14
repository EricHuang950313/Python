class Practice():
  def __init__(self):
    pass

  def First_TriangleDistinguish(self, a, b, c):
    l = sorted([a, b, c])
    for i in l:
      print(i, end=" ")
    print()
    if l[0]+l[1] <= l[2]:
      print("No")
    elif l[0]**2 + l[1]**2 > l[2]**2:
      print("Obtuse")
    elif l[0]**2 + l[1]**2 == l[2]**2:
      print("Right")
    elif l[0]**2 + l[1]**2 < l[2]**2:
      print("Acute")

  def Second_BiggestSum(self, l):
    result, ava = 0, []
    for i in range(len(l)):
      result += max(l[i])
    for j in range(len(l)):
      if result % max(l[j]) == 0:
        ava += [max(l[j])]
      else:
        continue
    print(result)
    if len(ava) == 0:
      print(-1)
    else:
      for i in ava:
        print(i, end=" ")

  def Third_KBomb(self, n, m, k):
    people_list = [i+1 for i in range(n)]
    index = 0
    for i in range(k):
      index = (index+m-1)%len(people_list)
      people_list.pop(index)
      if index == len(people_list):
        index = 0
    print(people_list[index])

  def Forth_BaseballGame(self, data, out):
    inning_out = 0
    score = 0
    base = [0]*3
    for i in range(1, data[0][0]+1):
      for j in range(9):
        if (data[j][0] < data[0][0]) and (i == data[0][0]):
          break
        if data[j][i] == "HR":
          score += base[0]+base[1]+base[2]+1
          base = [0]*3
        elif data[j][i] == "3B":
          score += base[0]+base[1]+base[2]
          base = [0, 0, 1]
        elif data[j][i] == "2B":
          score += base[1]+base[2]
          base = [0, 1, base[0]] 
        elif data[j][i] == "1B":
          score += base[2]
          base = [1, base[0], base[1]]
        elif data[j][i] == "FO" or "GO" or "SO":
          inning_out += 1
          if inning_out == 3:
            base[0] = base[1] = base[2] = 0
            inning_out = 0
          out -= 1
          if out == 0:
            break
      if out == 0:
            break
    print(score)
          

practice = Practice()
#1
# inputA = input().split()
# practice.First_TriangleDistinguish(int(inputA[0]), int(inputA[1]), int(inputA[2]))
#2
# times, amount = input().split()
# times, amount, sl = int(times), int(amount), []
# for i in range(times):
#   sl += [list(map(int, input().split()))]
# practice.Second_BiggestSum(sl)
#3
# user_nmk = input().split()
# n, m, k = map(int, user_nmk)
# practice.Third_KBomb(n, m, k)
#4
# fl = []
# for i in range(9):
#   user_input = input().split()
#   fl += [list(map(str, user_input))]
#   fl[i][0] = int(fl[i][0])
# out = int(input())
# practice.Forth_BaseballGame(fl, out)