from solution.irrational_decimal import get_fraction_digits

digit_one = int(get_fraction_digits(1)[-1])
digit_two = int(get_fraction_digits(10)[-1])
digit_three = int(get_fraction_digits(100)[-1])
digit_four = int(get_fraction_digits(1000)[-1])
digit_five = int(get_fraction_digits(10000)[-1])
digit_six = int(get_fraction_digits(100000)[-1])
digit_seven = int(get_fraction_digits(1000000)[-1])

solution = digit_one * digit_two * digit_three * digit_four * digit_five * digit_six * digit_seven
print('The solution for Problem 40 is {}'.format(solution))
