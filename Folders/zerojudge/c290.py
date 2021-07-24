user = input()
a, b = list(map(int, user[0::2])), list(map(int, user[1::2]))
print(abs(sum(a)-sum(b)))