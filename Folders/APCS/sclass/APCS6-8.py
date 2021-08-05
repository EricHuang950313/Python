import sys

dic = {"A":0, "B":0, "C":0}

for s in sys.stdin:
    vote = int(s)
    if vote == 1:
        dic["A"] = dic["A"]+1
    elif vote == 2:
        dic["B"] = dic["B"]+1
    elif vote == 3:
        dic["C"] = dic["C"]+1
    else:
        pass
    print(dic)