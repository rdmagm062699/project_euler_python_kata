from .name import score_name

def score_list_of_names(names): 
    score = 0

    for (pos, name) in enumerate(names):
        score += score_name(name, pos + 1)

    return score
