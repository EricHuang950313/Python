import sys

for s in sys.stdin:
    user = s.split(" ")
    if user[0]+user[1]>user[2] and user[1]+user[2]>user[0] and user[0]+user[2]>user[1]:
        print("yes")
    else:
        print("no")