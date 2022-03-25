user = input()
for i in range(len(user)//2):
  if user[i] != user[len(user)-i-1]:
    print('no')
    break
else:
  print('yes')