
NUMBER_NAMES = {
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five", 
    6: "six",
    7: "seven",
    8: "eight", 
    9: "nine",
    10: "ten", 
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
    20: "twenty",
    30: "thirty",
    40: "forty",
    50: "fifty",
    60: "sixty",
    70: "seventy",
    80: "eighty",
    90: "ninety"
}

def get_number_name(number):
    name = ""

    if number >= 100:
        name = "{} hundred".format(NUMBER_NAMES[number // 100])
        number = 0

    if number > 20:
        name = NUMBER_NAMES[number - (number % 10)]
        number %= 10
        name += "-" if number > 0 else ""

    if number > 0:
        name += NUMBER_NAMES[number]

    return name
