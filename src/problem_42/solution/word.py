
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def get_word_value(word):
    value = 0
    for letter in word:
        letter_num = LETTERS.index(letter) + 1
        value += letter_num

    return value
