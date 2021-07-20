import sys

for s in sys.stdin:
    user = int(s)
    if user % 2 == 0:
        print("even")
    else:
        print("odd")