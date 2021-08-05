a, b = input().split()
a, b = int(a), int(b)
n = int(input())
l = []
result = 0
for i in range(n):
    user = input().split()
    user = list(map(int, user))
    l.append(user)
    if (l[i].count(a)-l[i].count(-a))>0 and (l[i].count(b)-l[i].count(-b))>0:
        result += 1

print(result)