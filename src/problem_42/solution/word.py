from .number import is_triangle_number


LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def is_triangle_word(word):
    word_value = get_word_value(word)

    return is_triangle_number(word_value);


def get_word_value(word):
    value = 0
    for letter in word:
        letter_num = LETTERS.index(letter) + 1
        value += letter_num

    return value
