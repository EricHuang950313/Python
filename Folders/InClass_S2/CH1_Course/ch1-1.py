class Action:
    def __init__(self):
        self.position = [0, 0]
        self.times = 1
        pass
    
    def up(self, n):
        p = self.position
        p[1] += n
        self.position = p

    def down(self, n):
        p = self.position
        p[1] -= n

    def left(self, n):
        p = self.position
        p[0] -= n

    def right(self, n):
        p = self.position
        p[0] += n

    def show(self):
        print("Current Position :", self.times, self.position)
        self.times += 1

x = Action()
x.up(3)
x.show()
x.right(4)
x.show()