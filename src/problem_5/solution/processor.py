
def check_all_divisors(dividend, max_divisor):
    result = True
    for divisor in range(max_divisor, 0, -1):
        if dividend % divisor != 0:
            result = False
            break
   
    return result

def get_divisors_to_check(max_divisor):
    possible_divisors = list(range(max_divisor, 0, -1))
    result = [divisor for divisor in possible_divisors if _is_divisor_we_check(divisor, max_divisor)]
    
    return result

def _is_divisor_we_check(divisor, max_divisor):
    if divisor == max_divisor:
        return True
    
    result = True
    for check in range(divisor + 1, max_divisor + 1):
        if check % divisor == 0:
            result = False

    return result
