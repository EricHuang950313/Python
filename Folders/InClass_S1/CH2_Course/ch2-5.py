def change_x():
    global x
    x = 6

x = 5
print("x before:{}".format(x))

change_x()

#if第二行沒有"global x" x依然是5
print("x after:{}".format(x))
