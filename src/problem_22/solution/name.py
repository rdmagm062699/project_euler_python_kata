
LETTERS = 'ABC'

def score_name(name, multiplier): 
    score = 0

    for letter in name:
        pos = LETTERS.index(letter) + 1
        score += pos

    return score
