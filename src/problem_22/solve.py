from solution.calculate import score_list_of_names
import pathlib

path = "{}/names.txt".format(pathlib.Path(__file__).parent.absolute())

solution = 0

with open(path, "r") as f:
    data = f.read()
    names = [name.replace('"', '') for name in data.split(',')]
    solution = score_list_of_names(names)

print('The solution for Problem 22 is {}'.format(solution))
