import sys

for s in sys.stdin:
    if int(s) > 80:
        print("A")
    elif 60 <= int(s) <= 79:
        print("B")
    else:
        print("C")