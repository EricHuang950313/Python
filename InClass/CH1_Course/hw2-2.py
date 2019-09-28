print("== Start ==")
print()

print("-- The next \"n\" lines have one English word per line,"+ 
" and each word has a length of no more than 100.")

print("-- The last line has \"m\" positive integers replaced with blanks,"
" and the number provided does not exceed the total length of the string.")

print()

NandM = input("Please Input \"n m\".").split()
n, m = NandM[0], NandM[1]

wordlist = []

for i in range(int(n)):
    i = input()
    wordlist += i

m1 = input().split()


for i in range(int(m)):
    print(wordlist[int(m1[i])-1], end="")