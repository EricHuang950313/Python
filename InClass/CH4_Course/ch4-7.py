import math
class fraction():
    def __init__(self, numerator, denominator):
        self.n = numerator
        self.d = denominator
        pass

    def __str__(self):
        return ("{}/{}".format(self.n, self.d))

    def __add__(self, other):
        n = self.n*other.d + other.n*self.d
        d = self.d*other.d
        return ("{}/{}".format(n, d))

    def Devide(self, A, B):
        C = max(A, B)
        D = min(A, B)

        temp = 0
        for i in range(D):
            if D%(i+1)==0 and C%(i+1)==0:
                if (i+1)>temp:
                    temp = (i+1)
        return temp


F1 = fraction(2, 3)
F2 = fraction(1, 9)

print(F1 + F2)
before = F1 + F2
x = math.floor(len(before)/2)
A = int(before[:x])
B = int(before[x+1:])
temp = F1.Devide(A, B)
print("{:.0f}/{:.0f}".format(A/temp, B/temp))
