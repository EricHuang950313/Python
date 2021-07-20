import random, sys

for s in sys.stdin:
    count = 0
    if int(s) == 1:
        r = random.randint(1, 6)
        print(r)
        count += r
    else:
        for i in range(int(s)):
            r = random.randint(1, 6)
            print(r, end=" ")
            count += r
        print()
    print(count)