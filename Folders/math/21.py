import sympy as sy 
x = sy.Symbol("x")
y = sy.Symbol("y")
print(sy.solve([7*x+11*y-20, 11*x+7*y-52], [x,y]))

a = sy.Symbol("a")
b = sy.Symbol("b")
print(sy.solve([-6*a-10-20,18+2*b-42], [a,b]))