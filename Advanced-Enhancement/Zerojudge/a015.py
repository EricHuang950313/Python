import sys
for s in sys.stdin:
  result = list(map(int, s.split(" ")))
  l = []
  for i in range(int(result[1])):
    l.append([])
  for i in range(int(result[0])):
    result = input().split(" ")
    for j in range(len(l)):
      l[j].append(result[j])
  for i in range(len(l)):
    for j in range(len(l[j])):
      print(l[i][j], end=" ")
    print()
