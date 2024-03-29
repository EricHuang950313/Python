class Practice():
  def __init__(self):
    pass

  def First_LogicOperators(self, a, b, result):
    def check_AND(a, b):
        return 1 if a!=0 and b!=0 else 0
    def check_OR(a, b):
        return 0 if a==0 and b==0 else 1
    def check_XOR(a, b):
        return 1 if a==0 and b!=0 or a!=0 and b==0 else 0
    if check_AND(a, b) == result:
        print("AND")
    if check_OR(a, b) == result:
        print("OR")
    if check_XOR(a, b) == result:
        print("XOR")  
    if check_AND(a, b) != result and check_OR(a, b) != result and check_XOR(a, b) != result:
        print("IMPOSSIBLE")

  def Second_AlternatingStrings(self, a, b):
    b = [ 1 if i.isupper() else 0 for i in b ]
    maxx, status, count, nowindex = 0, True, 0, 0
    for i in range(len(b)):
      now = b[i]
      while status:
        for j in range(a):
          if b[i+nowindex] == now:
            count += 1
          else:
            status = False
            break
          if (i+nowindex)+1 == len(b):
            status = False
            break
          nowindex += 1
        else:
          if count > maxx:
            maxx = count
        now = 0 if now==1 else 1
      status, count, nowindex = True, 0, 0
    print(maxx)
    
  def Third_TreeAnalyses(self, n, data):
    def nodeh(data, node):
      biggest = 0
      if data[node-1][1] == 0:
        return 0
      else:
        for i in range(2, data[node-1][1]+2):
          temp = nodeh(data, data[node-1][i])+1
          biggest = max(temp, biggest)
        return biggest
    root = total = highest = 0
    for i in range(1, n+1):
      hi = nodeh(data, i)
      if hi > highest:
        highest = hi
        root = i
      total += hi
    print(root)
    print(total)

  def Forth_Stacking(self, n, w, f):
    items = [list(map(int, [w[i], f[i]])) for i in range(len(w))]
    for i in range(n-1):
      for j in range(n-1-i):
        if items[j][0]*items[j+1][1] > items[j+1][0]*items[j][1]:
          items[j], items[j+1] = items[j+1], items[j]
    print(items)
    summ, minn = 0, 0
    for k in range(n-1):
      summ += items[k][0]
      minn += summ*items[k+1][1]
    print(minn)

practice = Practice()
#1
# user_list = input().split()
# a, b, result = map(int, user_list)
# practice.First_LogicOperators(a, b, result)
#2
# a = int(input())
# b = input()
# if len(b) == 1:
#   print(1)
# else:
#   practice.Second_AlternatingStrings(a, b)
#3
# n = int(input())
# data = []
# for i in range(n):
#   user_input = input().split()
#   data += [[i+1, int(user_input[0])]]
#   if int(user_input[0]) > 0:
#     for j in range(2, int(user_input[0])+2):
#       data[i] += [int(user_input[j-1])]
# practice.Third_TreeAnalyses(n, data)
#4
# n = int(input())
# w = input().split()
# f = input().split()
# practice.Forth_Stacking(n, w, f)  