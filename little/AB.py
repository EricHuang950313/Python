import random
A = 0
B = 0
num = ("123456789")
p = (random.sample(num,4))
computer = (p[0],p[1],p[2],p[3])
player = input("請輸入四個不同的數字:")
while (player != computer):
  A = 0
  B = 0
  for i in range(4):
    if computer[i] == player[i]:
        A += 1
    else:
     for j in range(4):
        if player[i] == computer[j]:
            B += 1
  print("{}A{}B".format(A, B))
  if (A == 4):
      break
  player = input("請輸入四個不同的數字:")
print("The Answer Is {}{}{}{}".format(p[0],p[1],p[2],p[3]))
