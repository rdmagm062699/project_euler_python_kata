
def get_eligible_numbers(max_number):
    return [number for number in range(max_number) if _is_eligible(number)]

def _is_eligible(number):
    return number > 0 and (number % 3 == 0 or number % 5 == 0)
