
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def is_triangle_word(word):
    return True;


def get_word_value(word):
    value = 0
    for letter in word:
        letter_num = LETTERS.index(letter) + 1
        value += letter_num

    return value
