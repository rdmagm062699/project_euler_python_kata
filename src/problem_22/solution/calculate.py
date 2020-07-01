from .name import score_name

def score_list_of_names(names): 
    score = 0

    pos = 1
    for name in names:
        score += score_name(name, pos)
        pos += 1

    return score
