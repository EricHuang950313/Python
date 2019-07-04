def sum_scores(scores):
    try:
        count = 0
        sum = 0
        for i in scores:
            sum += i
            count += 1
    except TypeError:
        return 0, 0
    else:
        return sum, count

scores = [94, 93, 91, 100, 90]

sum = sum_scores(scores)
print("Sum", sum)
print("Avarage",sum[0]/sum[1])