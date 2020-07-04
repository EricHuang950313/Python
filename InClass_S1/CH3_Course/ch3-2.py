class People: # 模板 -> 建立物件
    def __init__(self, n, b, h, w, r): 
        # 類別初始化 -> 一定執行 -> 可建立基本資料
        # self.XX 是指物件 XX 本身的變數
        # self.name 是物件 p1 本身的變數
        self.name = n
        self.birthyear = b
        self.height = h
        self.weight = w
        rrr = r # 函式本身的區域變數，不屬於物件

p1 = People("Eric", "0313", 165, 55, 111)
print(p1.name)

p2 = People("Bala", "0000", 1, 2, 3)
print(p2.name)