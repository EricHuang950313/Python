#儲存檔案
file = open("data_a.txt", mode="w", encoding="utf-8")  #開啟
file.write("Hello World\nSecond line")  #操作
file.write("中文\n好棒棒")
file.close()  #關閉
