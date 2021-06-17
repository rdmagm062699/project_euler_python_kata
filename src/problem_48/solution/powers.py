
def get_power_sequence_sum(start, end):
    total = 0
    
    for num in range(start, end + 1):
        total += num ** num

    return total
