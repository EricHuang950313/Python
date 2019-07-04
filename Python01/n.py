# 1 infomation, in the last.
l = ["Eric", 12, "Gsw", "apple", 30, 34, 0, 35, 11, "happy"]
print(l)
l.append("Angel")
l.append([50, 60])
print(l)
print("===========")
# Many infomation in the last
x = 10, 20
print(type(x))
l.extend(x)
print(l)
l.extend([50,60])
print(l)
print("===========")
# choose the place
l.insert(2, 600) # from 0
print(l)
print("===========")
# remove 
l.remove(600)
print(l)
print("===========")
# choose place
l.pop(11)
print(l)
print("===========")
# all away
l.clear()
print(l)