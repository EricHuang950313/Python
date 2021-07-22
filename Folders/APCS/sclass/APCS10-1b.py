import sys

for s in sys.stdin:
    s = s.split()
    count = 0
    for i in s:
        count += int(i)
    print(count/len(s))