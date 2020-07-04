class ListStack():
    def __init__(self, data=[]):  # 允許使用者不輸入data，就會預設是空的
        self.data = data

    def __len__(self):
        return len(self.data)

    def is_empty(self):
        return len(self.data) == 0

    def push(self, e):
        self.data += [e]
        return self.data

    def pop(self):
        if len(self.data) == 0:
            take_out = []
            print("You can't take out, because the stack is empty!")
        else:
            take_out = self.data[-1]
            self.data = self.data[:-1]
        return take_out, self.data

stack = ListStack(["BMW", "Benz"])
print(stack.data)
data = stack.push("Nissan")
print(data)
data = stack.push("Toyota")
print(data)
take_out, data = stack.pop()
print(data)