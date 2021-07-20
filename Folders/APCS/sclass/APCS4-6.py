import sys

for s in sys.stdin:
    v = int(input())
    if ((v % 4 == 0) and (v % 100 != 0)) or (v % 400 == 0):
        print("閏年")
    else:
        print("平年")