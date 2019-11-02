# import time
# a = time.time()
# time.sleep(3)
# b = time.time()
# print(b-a)

import datetime
today = datetime.datetime.today()
print(today.date())
print(today.year)
print(today.month)
print(today.day)
print(today.hour)
print(today.minute)
print(today.second)

some_date = datetime.datetime(2019, 2, 2) # 創造某一天

print(some_date)
print(some_date - today)
print(today + datetime.timedelta(50)) # 距離今天50天後