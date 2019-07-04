# 抓網頁
import requests as re
from bs4 import BeautifulSoup as be

web = re.get("https://erichuang950313.github.io/nba_web/main/homepage.html")
print(web.status_code)
#status_code 傳送狀態
#200是ok
#https://blog.miniasp.com/post/2009/01/16/Web-developer-should-know-about-HTTP-Status-Code.aspx
a = be(web.text, "html.parser")
print(a.find_all("",{"id":"a"}))
print(a.find("",{"id":"a"}).text)
# "" 不能去掉
# "" 標籤名稱