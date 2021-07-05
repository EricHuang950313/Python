a = int(input())
s = ""
i = 2
p = 1
while a != 1:
    if a%i == 0:
        if p == 1:
            s += (str(i)+" * ")
        elif p == 2:
            s = s[:-3]
            s += ("^"+str(p)+" * ")
        else:
            s = s[:-4-int(len(str(p-1)))]
            s += ("^"+str(p)+" * ")
        p += 1
        a /= i
    else:
        p = 1
        i += 1
print(s[:-3])