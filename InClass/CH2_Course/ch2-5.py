def change_x():
    global x
    x = 6

x = 5
print("x before:{}".format(x))

change_x()

print("x after:{}".format(x))