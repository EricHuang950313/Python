quene = []

def enquene(data):
    quene.append(data)
def dequene():
    if isempty() != True:
        result = quene.pop(0)
        return result
    return None
def isempty():
    return True if len(quene)==0 else False
def front():
    return quene[0] if isempty() == False else -1

n = int(input())
for i in range(n):
    user = input().split()
    if user[0] == "1":
        enquene(user[1])
    elif user[0] == "2":
        print(front())
    elif user[0] == "3":
        dequene()