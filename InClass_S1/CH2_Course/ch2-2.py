a = 5
b = 4
c = 3
l = 0

if a > b:
    l = b
    b = a
    a = l
if b > c:
    l = c
    c = b
    b = l     
if a > b:
    l = b
    b = a
    a = l   
print(a,b,c)