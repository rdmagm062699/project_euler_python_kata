
def check_all_divisors(dividend, max_divisor):
    result = True
    for divisor in range(max_divisor, 0, -1):
        if dividend % divisor != 0:
            result = False
            break
   
    return result

def get_divisors_to_check(max_divisor):
    return [*range(2, max_divisor+1)]