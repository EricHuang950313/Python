v = ["a", "e", "i", "o", "u"]
count = 0

user = input()
for i in user:
    if i in v:
        count += 1
    else:
        pass
print(count)