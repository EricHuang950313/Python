from classes.parent import *

class Child(Parent):
    def __init__(self):
        super().__init__()

        self.public_var = 'Child類別的公開變數'
        self._protected_var = 'Child類別的保護變數'

    def get_super_public_var(self):
        return self.public_var

    def get_super_protected_var(self):
        return self._protected_var

    def get_super_private_var(self):
        return self.__private_var

    def call_super_public_method(self):
        return self.public_method()

    def call_super_protected_method(self):
        return self._protected_method()

    def call_super_private_method(self):
        return self.__private_method()

    def public_method(self):
        return 'Child類別的公開方法'
