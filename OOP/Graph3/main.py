import shape as sh

# 建立Circle、Rectangle和Triangle類別的物件
c = sh.Circle(10)
r = sh.Rectangle(5, 2)
t = sh.Triangle(8, 3)

# 把物件加入Tuple資料組
shapes = c, r, t

# 用For迴圈顯示每一個物件的內容和面積
for s in shapes:
    s.show_shape_info()
    print('面積：' + str(s.get_area()))
