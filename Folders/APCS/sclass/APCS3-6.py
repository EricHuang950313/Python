import sys

for s in sys.stdin:
    date = s.split(" ")
    result = (int(date[0])+int(date[1]))%10
    print(result)