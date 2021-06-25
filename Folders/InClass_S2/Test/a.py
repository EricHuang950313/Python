class Quene():
    def __init__(self, data=[]):
        self.data = data

    def len_data(self):
        return len(self.data)

    def push(self, e):
        self.data += [e]
        return self.data

    def pop(self):
        if Quene.len_data == 0:
            print("The Quene is emtpy")
        else:
            take_out = self.data[0]
            self.data = self.data[1:]
            return take_out, self.data

main = Quene(["John", "Tony"])
main.push("Larson")
main.pop()
print(main.data)
main.pop()
print(main.data)
main.pop()
print(main.data)