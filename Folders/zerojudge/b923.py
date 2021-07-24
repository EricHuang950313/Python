stack = []

def push(data):
    stack.append(data)
    return stack
def pop():
    if empty() == True:
        return None
    else:
        result = stack.pop()
        return result
def top():
    return stack[len(stack)-1]
def size():
    return len(stack)
def empty():
    return True if len(stack)==0 else False

n = int(input())
for i in range(n):
    user = input().split()
    if user[0] == "1":
        pop()
    elif user[0] == "2":
        print(top())
    elif user[0] == "3":
        push(user[1])    
