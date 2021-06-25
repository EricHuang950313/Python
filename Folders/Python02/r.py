scores = [50, 52, 54, 56, 58, 60]
new = map(lambda x: 60 if 55 <= x < 60 else x, scores)

for i in new:
    print(i)