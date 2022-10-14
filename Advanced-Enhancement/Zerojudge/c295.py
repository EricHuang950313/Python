# user's input
digits = []
ch = []
chh = []
biggest = 0
n, m = input().split()
n = int(n)
m = int(m)
for i in range(1, n+1):
    userInput = input().split()
    userInput = list(map(int, userInput))
    digits.append(userInput)

# process
if n == 1:
    biggest += max(digits[0])
    ch += [max(digits[0])]
else:
    for i in range(n):
        biggest += max(digits[i])
        ch += [max(digits[i])]
for i in ch:
    if biggest % i == 0:
        chh += [i]

# print
print(biggest)
if len(chh) == 0:
    print(-1)
else:
    for i in chh:
        print(i, end=" ")