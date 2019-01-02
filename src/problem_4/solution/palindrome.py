
def is_palindrome(value):
    digits = [digit for digit in str(value)]
    if digits == list(reversed(digits)):
        return True

    return False
