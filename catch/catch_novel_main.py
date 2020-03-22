# 抓網頁
import requests as re
from bs4 import BeautifulSoup as be

xyz = "11683/10113034.html"
times = 1
novel = ""

while True:
    if times == 1001:
        break

    web = re.get("https://m.mzsw123.com/html/%s" %xyz)
    web.encoding = 'big5'
    #status_code 傳送狀態
    #200是ok
    #https://blog.miniasp.com/post/2009/01/16/Web-developer-should-know-about-HTTP-Status-Code.aspx
    a = be(web.text, "html.parser")

    novel += a.find("",{"id":"nr_title"}).text
    novel += a.find("",{"id":"nr"}).text

    with open("./novel/%s.txt" %times, mode="w", encoding="utf-8") as file:
        file.write(novel)
    
    novel = ""

    times += 1
    b = a.find_all("",{"id":"pb_next"})
    c = str(b[0])
    xyz = c[15]+c[16]+c[17]+c[18]+c[19]+c[20]+c[21]+c[22]+c[23]+c[24]+c[25]+c[26]+c[27]+c[28]+c[29]+c[30]+c[31]+c[32]

