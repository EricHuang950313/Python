import sys

for s in sys.stdin:
    a = 0
    b = 0
    for i in range(1, len(s)+1):
        if i % 2 == 0:
            a += ord(s[i-1])
        else:
            b += ord(s[i-1])
    result = abs(b-a)%5
    if result == 0:
        print("Lucky Ball")
    elif result == 1:
        print("Lucky Sheep")
    elif result == 2:
        print("Lucky Guy")
    elif result == 3:
        print("OK")
    elif result == 4:
        print("Good luck")