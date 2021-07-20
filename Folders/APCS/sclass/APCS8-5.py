import sys

def add(a, b):
    return a+b
def sub(a, b):
    return a-b
def mul(a, b):
    return a*b
def div(a, b):
    return a/b

for s in sys.stdin:
    user = s.split()
    try:
        if user[1] == "+":
            print(add(int(user[0]), int(user[2])))
        elif user[1] == "-":
            print(sub(int(user[0]), int(user[2])))
        elif user[1] == "*":
            print(mul(int(user[0]), int(user[2])))
        elif user[1] == "/":
            print(div(int(user[0]), int(user[2])))
    except BaseException:
        print("N/A")