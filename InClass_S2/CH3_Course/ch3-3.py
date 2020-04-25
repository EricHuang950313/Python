class ListStack:
    def __init__(self,data):
        self.data=data
    def push(self,elem):
        self.data.append(elem)
        return self.data
    def pop(self):
        if len(self.data)==0:
            takeout=[]
            print('The stack is empty')
        else :
            takeout = self.data[-1]
            self.data = self.data[:-1]
        return self.data, takeout
class ListQueue:
    def __init__(self,data):
        self.data=data
    def push(self,elem):
        self.data.append(elem)
        return self.data
    def pop(self):
        if len(self.data)==0:
            takeout=[]
            print('The stack is empty')
        else :
            takeout = self.data[0]
            self.data = self.data[1:]
        return self.data, takeout

stack1 = ListStack(['big','middle','small'])
stack2 = ListStack([])
stack3 = ListStack([])
# step1
data, takeout = stack1.pop()
stack3.push(takeout)

# step2
data, takeout = stack1.pop()
stack2.push(takeout)

# step3
data, takeout = stack3.pop()
stack2.push(takeout)

# step4
data, takeout = stack1.pop()
stack3.push(takeout)

# step5
data, takeout = stack2.pop()
stack1.push(takeout)

# step6
data, takeout = stack2.pop()
stack3.push(takeout)

# step7
data, takeout = stack1.pop()
stack3.push(takeout)