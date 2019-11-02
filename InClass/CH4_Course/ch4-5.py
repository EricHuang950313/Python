class People: 
    def __init__(self, n, b, h, w): 
        # 屬性
        self.name = n
        self.birthyear = b
        self.height = h
        self.weight = w
    def __add__(self, other):
        print(type(other))
        print(type(self))
        if type(other) == type(self):
            return self.weight + other.weight
        elif type(other) == int:
            return self.weight + other
        

p1 = People("AAA", 2002, 1.70, 70)
p2 = People("BBB", 2001, 1.75, 75)

# 如果用到 class -> 使用 overloading 的函式
# 如果沒有用到 class -> 使用原本的函式
print(p1 + p2)
print(1 + 2)

print(p1 + 2)