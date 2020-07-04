class Jump():
    def __init__(self, name, ability, distance):
        self.name = name
        self.ability = ability
        self.distance = distance
    def jump(self):
        self.distance += self.ability
        return self.distance

T1 = Jump("aaa", 1, 0)
T2 = Jump("bbb", 3, 0)
T3 = Jump("ccc", 5, 0)
T4 = Jump("ddd", 4, 0)
T5 = Jump("eee", 2, 0)

l = []
l += [T1, T2, T3, T4, T5]

for i in range(100):
    for j in range(len(l)):
        l[j].jump()
        if l[j].distance >= 100:
            print(l[j].name)
            break
    if l[j].distance >= 100:
        break