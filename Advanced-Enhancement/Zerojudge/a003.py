v = input().split(" ")
if (int(v[0])*2+int(v[1]))%3 == 0:
    print("普通")
elif (int(v[0])*2+int(v[1]))%3 == 1:
    print("吉")
else:
    print("大吉")