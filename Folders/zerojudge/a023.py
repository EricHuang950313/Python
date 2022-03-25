numbers = sorted(list(map(int, input().split())))
maxx, minn = numbers[1], numbers[0]
r = maxx % minn
while r != 0:
  maxx = minn
  minn = r
  r = maxx % minn
print(minn)