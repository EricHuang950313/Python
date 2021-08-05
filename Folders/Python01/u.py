all_scores_list = [100, 90, 96, 58]

pass_l = []
fail_l = []
pass_ = 0
fail_ = 0

for i in all_scores_list:
    if i >= 60:
        pass_ += 1
    else:
        fail_ += 1

pass_l += [pass_]
fail_l += [fail_]

for i in range(0, len(pass_l)):
    print("pass:", pass_l[i],"fail:", fail_l[i])