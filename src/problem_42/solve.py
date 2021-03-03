import pathlib
from solution.word import is_triangle_word

total_triangle_words = 0

file_path = '{}/p042_words.txt'.format(pathlib.Path(__file__).parent.absolute())
with open(file_path, 'r') as file:
    words = file.read()

for word in words.split(','):
    if is_triangle_word(word.replace('"', '')):
        total_triangle_words += 1

print('The solution for Problem 42 is {}'.format(total_triangle_words))
