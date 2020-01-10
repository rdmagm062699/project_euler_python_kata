
def check_all_divisors(dividend, max_divisor):
    result = True
    for divisor in range(max_divisor, 0, -1):
        if dividend % divisor != 0:
            result = False
            break
   
    return result

def get_divisors_to_check(max_divisor):
    result = [divisor for divisor in range(max_divisor, 0, -1) if _is_divisor_we_check(divisor, max_divisor)]
    
    return result

def _is_divisor_we_check(divisor, max_divisor):
    return divisor == max_divisor or max_divisor % divisor != 0
