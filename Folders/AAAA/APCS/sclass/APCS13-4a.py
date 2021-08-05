import random
number = random.randint(1, 100)

countA = 0
for i in range(1, 101):
    if i == number:
        countA += 1
        print("Find it:", i)
        print(countA)
        break
    else:
        countA += 1
print("====================================")

countB = 0
lower, upper, c = 0, 100, 50
while True:
    if c == number:
        print("Find it:", i)
        print(countB)
        break
    countB += 1
    if c < number:
        lower = c
    elif c > number:
        upper = c
    c = int((lower+upper)/2)