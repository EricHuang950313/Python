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

print(stack)
push("a")
push("b")
push("c")
pop()
push("d")
print(size())
print(stack)