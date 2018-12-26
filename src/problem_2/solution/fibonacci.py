
def get_fibonacci_up_to(upper_bound):
    if upper_bound < 3:
        return []
    
    return [number for number in range(1, upper_bound)]
