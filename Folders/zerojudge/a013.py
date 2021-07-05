l = [["I", "X", "C", "M"], ["V", "L", "D"]]
def valuein(x):
    digit = 0
    ll = ["IV", "IX", "XL", "XC", "CD", "CM"]
    lll = [2, 2, 20, 20, 200, 200]
    for i in range(len(x)):
        if x[i] == "I":
            digit += 1
        elif x[i] == "V":
            digit += 5
        elif x[i] == "X":
            digit += 10
        elif x[i] == "L":
            digit += 50
        elif x[i] == "C":
            digit += 100
        elif x[i] == "D":
            digit += 500
        else:
            digit += 1000
    for e in range(len(ll)):
        digit -= lll[e]*x.count(ll[e])
    return digit
def valueout(x):
    if x == 0:
        return "ZERO"
    x = str(x)
    out = ""
    re = ""
    a = 0
    for i in range(len(x)-1, -1, -1):
        if int(x[i]) < 4:
            out = l[0][a]*int(x[i]) + out
            a += 1
        elif int(x[i]) == 4:
            out = (l[0][a]+l[1][a]) + out
            a += 1
        elif int(x[i]) == 9:
            out = (l[0][a]+l[0][a+1]) + out
            a += 1
        else:
            out = (l[1][a]+l[0][a]*(int(x[i])-5)) + out
            a += 1
    return out

llll = []
while True:
    user_input = input().split(" ")
    if user_input[0] == "#":
        break
    llll.append(valueout(abs(valuein(user_input[0])-valuein(user_input[1]))))

for k in llll:
    print(k)     