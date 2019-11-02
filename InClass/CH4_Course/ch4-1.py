class BankAccount():
    def __init__(self, name, defaultkeyword, canTranster):
        self.name = name
        self.defaultKeyword = defaultkeyword
        self.balance = 0
        self.canTranster = canTranster
        pass
    def save(self, amount):
        if amount > 0:
            self.balance += amount
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
        else:
            print("Balance not enough.")
    def operation(self):
        Choose = input("Please Choose save or withdraw.")
        if Choose == "save":
            saveAmount = int(input("What amount do you want to save?"))
            self.save(saveAmount)
        elif Choose == "withdraw":
            withdrawAmount = int(input("What amount do you want to withdraw?"))
            self.withdraw(withdrawAmount)
        else:
            print("You enter either save or withdraw.")
    def keyword(self):
        userKeyword = int(input("What's your keyword?"))
        if self.defaultKeyword == userKeyword:
            self.operation()
        else:
            print("Password Error.")

P1 = BankAccount("AAA", 12345678, 0) # P1等同self
P1.keyword()
print(P1.balance)