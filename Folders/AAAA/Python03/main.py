import process.cheak as cheak
scores_str = input('請輸入5個數，數字之間加入空格：').split()

scores = [] 

while True:
    for n in scores_str:
        if n.isdigit():   
            scores += [int(n)]

        if len(scores) == 5:
            break

    if len(scores) < 5:
        scores_str = input('請繼續輸入：').split()
    else:
        break

print("Highest:", str(cheak.highest(scores)))
print("Lowest:", str(cheak.lowest(scores)))
print("Avarage:", str(cheak.avarage(scores)))
print("Pass:", list(cheak.pass_scores(scores)))
print("Fail:", list(cheak.fail_scores(scores)))