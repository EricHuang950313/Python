dd = ("Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun")
date = int(input())
day = input()
find = int(input())
print(dd[((find-date)%7+dd.index(day))%7])

