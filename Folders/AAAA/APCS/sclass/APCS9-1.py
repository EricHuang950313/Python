import sys

for s in sys.stdin:
    a, b = s.split()
    print("今天的氣溫是 {} 度, 天氣是 {} 天".format(a, b))