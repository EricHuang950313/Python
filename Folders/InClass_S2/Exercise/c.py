import random
class create_list():
    def __init__(self, n):
        self.n = n
        self.temp = list(range(1, self.n*self.n+1))

    def random_choice(self):
        digit = random.choice(self.temp)
        self.temp.remove(digit)
        return digit

    def create(self):
        l = []
        for i in range(self.n):
            l_add = []
            for j in range(self.n):
                l_add += [create_list.random_choice()]
            l+=[l_add]
        return l

create_list = create_list(5)
out = create_list.create()
print(out)
