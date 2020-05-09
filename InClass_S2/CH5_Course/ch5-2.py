import time
def gcd(a,b):
    while b:
        r = a % b
        a = b
        b = r
    return a
start1 = time.time()
ans1 = gcd(192,240)
end1 = time.time()
print("gcd:", ans1, "time cost:%1.8f" %(end1-start1))

def gcd_recursive(a, b):
    if a == 0:
        return b
    else:
        return gcd_recursive(b%a, a)
start2 = time.time()
ans2 = gcd_recursive(240, 192)
end2 = time.time()
print("gcd_recursive:", ans2, "time cost:%1.8f" %(end2-start2))