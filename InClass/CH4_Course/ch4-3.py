class People: 
    def __init__(self, n, b, h, w): 
        # 屬性
        self.name = n
        self.birthyear = b
        self.height = h
        self.weight = w
    def __str__(self):
        return ("Name:{} Birthyear:{} Height:{} Weight:{}"\
            .format(self.name, self.birthyear, self.height, self.weight))
    def __add__(self, other):
        return self.weight + other.weight

p1 = People("AAA", 2002, 1.70, 70)
# 沒加"def __str__"前: print(p1)
print(p1)