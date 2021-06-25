# The sum of odd number
sum = 0
for i in range(1, 101):
    if i % 2 == 0:
        continue
    sum += i
print(sum)