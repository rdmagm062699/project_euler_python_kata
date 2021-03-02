
def is_triangle_number(number):
    n = 1
    stop = False

    while stop == False:
        t_num = get_nth_triangle_number(n)
        if t_num >= number:
            stop = True
        else:
            n += 1

    return number == t_num

def get_nth_triangle_number(n):
    return (.5 * n) * (n + 1)