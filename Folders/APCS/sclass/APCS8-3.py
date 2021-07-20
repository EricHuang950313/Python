import sys

def v(a, b):
    return int(a)+int(b)
def ss(a, b):
    return a+b

for s in sys.stdin:
    data = s.split()
    if data[0] == "1":
        print(v(data[1], data[2]))
    elif data[0] == "2":
        print(ss(data[1], data[2]))