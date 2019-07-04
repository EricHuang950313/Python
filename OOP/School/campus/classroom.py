class Classrom:
    def __init__(self):
        self._students = []
    
    def add_student(self, student):
        self._students += [student]

    def delete_student(self, student):
        self._students.remove(student)

    def get_all_students(self):
        return self._students

    def clear(self):
        self._students.clear()
    
    def get_student_number(self):
        return len(self._students)
