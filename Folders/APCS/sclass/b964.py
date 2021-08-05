student_amount = int(input())
scores = input().split()
scores = list(map(int, scores))
scores.sort()
p, f = [], []
for i in range(len(scores)):
    if scores[i] >= 60:
        p.append(scores[i])
    else:
        f.append(scores[i])
for i in scores:
    print(i, end=" ")
print()
c = 0
if len(f) == 0:
    print("best case")
else:
    for i in f:
        if i > c:
            c = i
    print(c)
c = 100
if len(p) == 0:
    print("worst case")
else:
    for i in p:
        if i < c:
            c = i
    print(c)