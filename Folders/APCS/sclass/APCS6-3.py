import sys

for s in sys.stdin:
    a = s.split()
    for i in range(len(a)):
        a[i] = int(a[i])
    print(sum(a)/len(a))