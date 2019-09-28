NandM = input("").split()
n, m = NandM[0], NandM[1]

wordlist = []

for i in range(int(n)):
    i = input()
    wordlist += i

m1 = input().split()


for i in range(int(m)):
    print(wordlist[int(m1[i])-1], end="")