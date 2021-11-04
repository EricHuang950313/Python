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