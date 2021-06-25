count = 0

def fun():
    global count
    count += 1
for i in range(1,11):
    fun()

print(count)

c2 = 0

def f2():
    f2.c2 += 1
    print(f2.c2)
f2.c2 = 0

def f3():
    try:
        f3.count += 1
    except AttributeError:
        f3.count = 1
    print(f3.count)