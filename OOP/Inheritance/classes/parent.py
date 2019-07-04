class Parent:
    def __init__(self):
        self.public_var = "\'Parent\' 類別的公開變數"
        self._protected_var = "\'Parent\' 類別的保護變數"
        self.__private_var = "\'Parent\' 類別的私有變數"
    
    def public_method(self):
        return "\'Parent\' 類別的公開變數"
    
    def _protected_method(self):
        return "\'Parent\' 類別的保護變數"

    def __private_method(self):
        return "\'Parent\' 類別的私有變數"

# same
'''
    def public_method(self):
        return self.public_var
    
    def _protected_method(self):
        return self._protected_var

    def __private_method(self):
        return self.__private_var
'''