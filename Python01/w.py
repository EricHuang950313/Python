import random
print(random.random())
print(random.randint(1,31))
colors = ["red", "yellow", "blue"]
print(random.choice(colors))
print(random.sample(colors, 2))
num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(random.shuffle(num))
print(num)