num_class = int(input("Please input the class's quantity:"))

all_scores_list = []

for i in range(0,num_class):
    print("The", i+1, "th class")

    scores_list = []
    num_students = int(input("Please input the students' quantity:"))

    for i in range(0, num_students):
        scores = int(input("Please input the scores:"))
        scores_list += [scores]
    all_scores_list += [scores_list]

for i, scores_list in enumerate(all_scores_list):
    print("The", i+1, "th class's scores:", scores_list)