import d as stu

s = stu.Student('李大中', 200, -5, 90)
print(s)
print('學生成績：' + str(s.get_data()))

s.set_data('李大中', 70, 80, 90)
print('學生成績：' + str(s.get_data()))

a = stu.Student('李小中', 70, 100, 90)
print(a)
print('學生成績：' + str(a.get_data()))
print('學生人數：' + str(stu.Student.get_count()))