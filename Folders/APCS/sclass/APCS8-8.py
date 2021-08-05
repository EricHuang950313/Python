import datetime 

yeara, montha, daya = input().split(" ")
ta = datetime.datetime(int(yeara), int(montha), int(daya))

yearb, monthb, dayb = input().split(" ")
tb = datetime.datetime(int(yearb), int(monthb), int(dayb))

print(tb-ta)