import pytube
yt = pytube.YouTube("https://www.youtube.com/watch?v=dwDHdqrQKyU")
stream = yt.streams.get_by_itag("22")
stream.download("../Project01")
# 影片的路徑