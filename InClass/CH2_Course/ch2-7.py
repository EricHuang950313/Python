def bmi(height, weight):
    #print(height)
    #print(weight)
    # print(round(weight / (height*height), 1)) # round 四捨五入
    return round(weight / (height*height), 1)

x = bmi(1.65, 55)
y = bmi(1.8, 65)
z = bmi(1.7, 60)

print((x+y+z)/3)