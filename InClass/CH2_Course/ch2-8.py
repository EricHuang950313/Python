def bmi(height, weight):
    return round(weight / (height*height), 1)

def avg(x, y, z):
    return round((x+y+z)/3, 1)

x = bmi(1.65, 55)
y = bmi(1.8, 65)
z = bmi(1.7, 60)

print(avg(x,y,z))