import sys

for s in sys.stdin:
    a, b = s.split()
    b = int(b)
    for i in a:
        print(chr(ord(i)+b), end="")
    print()