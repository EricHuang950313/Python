# 抓網頁
import requests as re
from bs4 import BeautifulSoup as be

web = re.get("https://m.mzsw123.com/html/11683/4324910.html")
web.encoding = 'big5'

a = be(web.text, "html.parser")
b = a.find_all("",{"id":"pb_next"})
c = str(b[0])
print(c[15]+c[16]+c[17]+c[18]+c[19]+c[20]+c[21]+c[22]+c[23]+c[24]+c[25]+c[26]+c[27]+c[28]+c[29]+c[30]+c[31]+c[32])

