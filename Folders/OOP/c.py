class Student:
    _count = 0

    def __init__(self, name, ch_score, en_score, math_score):
        Student._count += 1

        self._name = name
        self._ch_score = Student._check_score(ch_score)
        self._en_score = Student._check_score(en_score)
        self._math_score = Student._check_score(math_score)
        
    @staticmethod
    def _check_score(score):
        if 0 <= score <= 100:
            return score
        else:
            return 0

    @staticmethod
    def get_count():
        return Student._count

s1 = Student("01", 80, 90, 100)
s2 = Student("02", 50, 60, 70)

print(str(Student.get_count()))