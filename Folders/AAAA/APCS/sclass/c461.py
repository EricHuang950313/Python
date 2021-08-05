import sys

def check_AND(a, b):
    return 1 if a!=0 and b!=0 else 0
def check_OR(a, b):
    return 0 if a==0 and b==0 else 1
def check_XOR(a, b):
    return 1 if a==0 and b!=0 or a!=0 and b==0 else 0

for s in sys.stdin:
    a, b, result = s.split()
    if check_AND(int(a), int(b)) == int(result):
        print("AND")
    if check_OR(int(a), int(b)) == int(result):
        print("OR")
    if check_XOR(int(a), int(b)) == int(result):
        print("XOR")  
    if check_AND(int(a), int(b)) != int(result) and check_OR(int(a), int(b)) != int(result) and check_XOR(int(a), int(b)) != int(result):
        print("IMPOSSIBLE")