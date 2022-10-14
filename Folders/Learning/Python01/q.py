num_list = [i for i in range(1, 11)]
print(num_list)
print("=======")
scores = [62, 60, 98, 100, 32, 11, 97]
allscores = [i for i in scores]
# allscores = scores.copy()
print(allscores)
la = [i for i in scores if i < 60]
print(la)
lb = [i+j for i in range(1, 6)for j in range(10,16)]
print(lb)
