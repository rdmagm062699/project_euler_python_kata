
def check_all_divisors(dividend, max_divisor):
    result = True
    for divisor in range(max_divisor, 0, -1):
        if dividend % divisor != 0:
            result = False
            break
   
    return result
