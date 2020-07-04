def sum1(*arg1):
    print(arg1)
def sum2(**arg2):
    print(arg2)
def sum3(*arg1, **arg2):
    print(arg1, arg2)

sum1(1,2,3)
sum2(a=1, b=2, c=3)
sum3(1,2,3,a=1)

print("==========")

def sum4(a, b, c):
    return a+b+c

args = {"a":1, "b":2, "c": 3}
print(sum4(**args))