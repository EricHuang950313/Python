quene = []
MAX_QUENE = 10

def enquene(data):
    quene.append(data)
def dequene():
    if isempty() != True:
        result = quene.pop(0)
        return result
    return None
def isempty():
    return True if len(quene)==0 else False
def isfull():
    return True if len(quene)==MAX_QUENE else False
def front():
    return quene[0]
def rear():
    return quene[len(quene)-1]

for i in range(11):
    if isfull() == False:
        enquene(i)
    else:
        print("Quene is full, can't add item.")

print(quene)