def highest(scores):
    return max(scores)


def lowest(scores):
    return min(scores)


def pass_scores(scores):
    return filter(lambda x: True if x >= 60 else False, scores)


def fail_scores(scores):
    return filter(lambda x: True if x <= 60 else False, scores)


def avarage(scores):
    return sum(scores) / len(scores)