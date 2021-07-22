def check(x, l):
    if x in l:
        return x
    else:
        return check(x-1, l)
while True:
    user = input().split()
    tl = [list(map(str, user[0::2])), list(map(int, user[1::2])), 4, 13]
    for i in range(len(tl[0])):
        if tl[0][i] == "A":
            tl[0][i] = 4
        elif tl[0][i] == "B":
            tl[0][i] = 3
        elif tl[0][i] == "C":
            tl[0][i] = 2
        elif tl[0][i] == "D":
            tl[0][i] = 1
    for i in range(2):
        digit = check(tl[i+2], tl[i])
        n = len(tl[i]) 
        for j in range(n):
            if i < 2:
                if tl[i][j-(n-len(tl[i]))] != digit:
                    tl[0].remove(tl[0][j-(n-len(tl[i]))])
                    tl[1].remove(tl[1][j-(n-len(tl[i]))])
    if tl[0][0] == 4:
        print("A", end=" ")
    elif tl[0][0] == 3:
        print("B", end=" ")
    elif tl[0][0] == 2:
        print("C", end=" ")
    elif tl[0][0] == 1:
        print("D", end=" ")
    print(tl[1][0])