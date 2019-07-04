import campus as ca
def show_students(classroom1, classroom2):
    print("Frist Classroom")
    for i in classroom1.get_all_students():
        print(i.get_data())

    print("Second Classroom")
    for i in classroom2.get_all_students():
        print(i.get_data())    

student1 = ca.Student("Student1", 100, 100, 100)
student2 = ca.Student("Student2", 90, 90, 90)
student3 = ca.Student("Student3", 80, 80, 80)
student4 = ca.Student("Student4", 70, 70, 70)
student5 = ca.Student("Student5", 60, 60, 60)

classroom1 = ca.Classrom()
classroom2 = ca.Classrom()

print("------Student in classroom------")
classroom1.add_student(student1)
classroom1.add_student(student2)
classroom1.add_student(student3)

classroom2.add_student(student4)
classroom2.add_student(student5)

show_students(classroom1, classroom2)

print("------Student leave classroom------")
classroom1.delete_student(student1)
classroom2.delete_student(student4)

show_students(classroom1, classroom2)

print("------Out of school------")
classroom1.clear()
classroom2.clear()

show_students(classroom1, classroom2)