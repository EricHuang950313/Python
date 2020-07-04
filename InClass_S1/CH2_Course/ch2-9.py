def bmi(height, weight):
    return round(weight / (height*height), 1)

def avg(*x):
    summ = 0
    for i in x:
        summ += i
    return summ/len(x)

x = bmi(1.65, 55)
y = bmi(1.8, 65)
z = bmi(1.7, 60)

print(avg(x,y,z))