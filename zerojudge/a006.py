import math
l = input().split(" ")
if (int(l[1])**2 - 4*int(l[0])*int(l[2])) > 0:
    print("Two different roots", "x1="+str(round((-int(l[1])+math.sqrt(int(l[1])**2 - 4*int(l[0])*int(l[2])))/(2*int(l[0])))), ",", "x2="+str(round((-int(l[1])-math.sqrt(int(l[1])**2 - 4*int(l[0])*int(l[2])))/(2*int(l[0])))))
elif (int(l[1])**2 - 4*int(l[0])*int(l[2])) == 0:
    print("Two same roots", "x="+str(round((-int(l[1])+math.sqrt(int(l[1])**2 - 4*int(l[0])*int(l[2])))/(2*int(l[0])))))
else:
    print("No real root")