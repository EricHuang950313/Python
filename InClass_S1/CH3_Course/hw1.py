def float(x):
    # decompose: n=int m=float
    x = x.split(".")
    l = x[0], x[1]

    a = int(len(l[0]), l[0])
    b = int(len(l[1]), l[1])
    b = b/(10**len(l[1]))

    return a+b
    

def int(n, s):
    # n=len(l[0]) s=l[0] or ...
    total = 0
    for i in range(n):
        if s[i] == "1":
            total += 1*(10**(n-1))
            n -= 1
        if s[i] == "2":
            total += 2*(10**(n-1))
            n -= 1
        if s[i] == "3":
            total += 3*(10**(n-1))
            n -= 1
        if s[i] == "4":
            total += 4*(10**(n-1))
            n -= 1
        if s[i] == "5":
            total += 5*(10**(n-1))
            n -= 1
        if s[i] == "6":
            total += 6*(10**(n-1))
            n -= 1
        if s[i] == "7":
            total += 7*(10**(n-1))
            n -= 1
        if s[i] == "8":
            total += 8*(10**(n-1))
            n -= 1
        if s[i] == "9":
            total += 9*(10**(n-1))
            n -= 1
        if s[i] == "0":
            total += 10*(10**(n-1))
            n -= 1
    return total

x = input()
print(type(x))
ans = float(x)
print(ans, type(ans))

# int -> str  e.g. 123/100 抓整數位 轉換成字串 再把它加起來