import sys

l = [4, 3, 2, 1]

for s in sys.stdin:
    user = s.split()
    if user[0] == "1":
        print(len(l))
    elif user[0] == "4":
        l.sort()
        print(l)
    elif user[0] == "2":
        l.append(int(user[1]))
        print(l)
    elif user[0] == "3":
        l.remove(int(user[1])) 
        print(l)