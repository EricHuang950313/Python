class People: 
    def __init__(self, n, b, h, w): 
        # 屬性
        self.name = n
        self.birthyear = b
        self.height = h
        self.weight = w

    def bmi(self):
        # 讓程式知道 方法 是屬於物件本身的
        # 如果沒有 self，就不能使用 self.weight、self.height
        self.qwer = 10 # 可新增(也可改變)
        return self.weight/(self.height**2)
    
    def get_bmi(self):
        print(self.bmi())

p1 = People("Eric", "0313", 1.65, 55)
p1.get_bmi()
p1.bmi() #要先執行
print(p1.qwer) # 才會出現