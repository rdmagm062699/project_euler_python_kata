
class Collatz:

    def __init__(self):
        self.cache = {}

    def get_sequence(self, starting_number):
        next_number = starting_number
        sequence = [next_number]
        stop = False

        while stop == False:
            next_number = self._get_next_number(next_number)

            if self.cache.get(next_number):
                sequence = sequence + self.cache[next_number]
                stop = True
            else:
                sequence.append(next_number)
                stop = True if next_number <= 1 else False

        if starting_number > 1:
            self.cache[starting_number] = sequence

        return sequence


    def _get_next_number(self, n):
        if n % 2 == 0:
            return n / 2
        else:
            return (3 * n) + 1