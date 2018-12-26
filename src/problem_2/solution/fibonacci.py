
def get_fibonacci_up_to(upper_bound):
    if upper_bound < 3:
        return []
    
    fibonacci = [1, 2]
    next_num = 3
    while next_num < upper_bound:
        fibonacci.append(next_num)
        next_num = fibonacci[-2] + fibonacci[-1]

    return fibonacci
