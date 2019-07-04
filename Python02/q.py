scores = [40, 50, 60, 70, 80]

f = lambda x: True if x < 60 else False

fail = filter(f, scores)

for i in fail:
    print(i, end=" ")

fs = filter(lambda x: True if x < 60 else False, scores)

for i in fs:
    print(i, end=" ")