#self.的設定 就代表你之後可以用的class屬性
class Student:
    _count = 0

    def __init__(self, name, ch_score, en_score, math_score):
        Student._count += 1

        # 呼叫set_data()方法儲存資料
        self.set_data(name, ch_score, en_score, math_score)

    # 取得物件個數。因為不需要用到self參數，所以設定為靜態方法
    @staticmethod
    def get_count():
        return Student._count

    # 儲存學生資料
    def set_data(self, name, ch_score, en_score, math_score):
        self._name = name
        self._ch_score = Student._check_score(ch_score)
        self._en_score = Student._check_score(en_score)
        self._math_score = Student._check_score(math_score)

    # 取得學生資料
    def get_data(self):
        return self._name, self._ch_score, \
               self._en_score, self._math_score

    # 這是私有方法，用來檢查成績是否合法
    # 因為不需要用到self參數，所以設定為靜態方法
    @staticmethod
    def _check_score(score):
        if 0 <= score <= 100:
            return score
        else:
            return 0

    # 這個方法會在執行print()的時候呼叫，取得要顯示字串
    def __str__(self):
        return self._name