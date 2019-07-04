# 抓網頁
import requests as re
from bs4 import BeautifulSoup as be

web = re.get("http://winter.cpbl.com.tw/cpbl.html")
print(web.status_code)
#status_code 傳送狀態
#200是ok
#https://blog.miniasp.com/post/2009/01/16/Web-developer-should-know-about-HTTP-Status-Code.aspx
a = be(web.text, "html.parser")
#print(a)
print(a.find("li").find("a").text)
# find 找第一個
print(a.find_all("li"))
# find_all 所有的