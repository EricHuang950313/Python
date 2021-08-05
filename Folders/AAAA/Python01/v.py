scores = [i for i in range(0, 501, 50)]
print(scores)
sorted_scores = []

for i in range(0, len(scores)):
    max_score = 0
    max_score_index = 0

    for j, data in enumerate(scores):
        if data > max_score:
            max_score = data   
            max_score_index = j
    highest_scores = scores.pop(max_score_index)
    sorted_scores += [highest_scores]
    
print(sorted_scores)