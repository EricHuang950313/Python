a = b = c = 0

# while (a == 0) or (b == 0) or (c == 0) or (a+b<c) or (b+c<a) or (a+c>b):

a = int(input("Please input A."))
b = int(input("Please input B."))
c = int(input("Please input C."))

if (a+b>c) and (b+c>a) and (a+c>b):
    print("Yes")
else:
    print("NO")