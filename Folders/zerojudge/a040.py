m, n = list(map(int, input().split()))
data = []
for i in range(m, n+1):
  if i == sum([int(j)**len(str(i)) for j in str(i)]):
    data += [i]
if len(data) == 0:
  print("none")
else:
  for k in data:
    print(k, end=" ")  