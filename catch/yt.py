# 抓 YOUTUBE
#https://python-pytube.readthedocs.io/en/latest/
import pytube
yt = pytube.YouTube("https://www.youtube.com/watch?v=MMmOLN5zBLY")
print(yt.streams.all())
# 結果 : 影片的格式
stream = yt.streams.get_by_itag("22")
# itag
stream.download("../Project01")
# 影片的路徑