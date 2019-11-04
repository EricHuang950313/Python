import math
class fraction():
   def __init__(self, numerator, denominator):
       self.n = numerator
       self.d = denominator
       pass
 
   def __add__(self, other):
       n = self.n*other.d + other.n*self.d
       d = self.d*other.d
       temp = self.Devide(n,d)
       return ("{:.0f}/{:.0f}".format(n/temp, d/temp))
 
 
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
