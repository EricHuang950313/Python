class Person:
    def __init__(self, name):
        self._name = name
        
    def set_name(self, name):
        self._name = name
        
    def get_name(self):
        return self._name

class Student(Person):
    def __init__(self, name, ch_score, en_score, math_score):
        super().__init__(name)
        self.set_score(ch_score, en_score, math_score)

    def set_score(self, ch_score, en_score, math_score):
        self._ch_score = ch_score
        self._en_score = en_score
        self._math_score = math_score

    def get_score(self):
        return self._ch_score, self._en_score, self._math_score

s = Student("S01", 90, 95, 100)
print(s.get_name())
print(s.get_score())

s.set_name("S02")
s.set_score(95, 100, 100)
print(s.get_name())
print(s.get_score())