n = int(input())
score = 0
if n < 40:
  for i in range(0, n):
    if i+1 >= 0 and i+1 <= 10:
      score += 6
    elif i+1 >= 11 and i+1 <= 20:
      score += 2
    elif i+1 >= 21 and i+1 <= 39:
      score += 1
else:
  score = 100
print(score)