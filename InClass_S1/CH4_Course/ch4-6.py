class People: 
    def __init__(self, n, b, h, w): 
        # 屬性
        self.name = n
        self.birthyear = b
        self.height = h
        self.weight = w
    def __eq__(self, other):
        # return True or False
        return self.birthyear == other.birthyear
        

p1 = People("AAA", 2002, 1.70, 70)
p2 = People("BBB", 2001, 1.75, 75)

print(p1 == p2)
