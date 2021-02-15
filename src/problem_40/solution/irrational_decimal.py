
def get_fraction_digits(length):
    digits = '0123456789'

    if length < 10:
        return digits[1:length + 1]
    else:
        value = '123456789'
        nextStart = 1
        while len(value) < length:
            nextChunk = ''.join([str(nextStart) + digit for digit in digits])
            value += nextChunk
            nextStart += 1

        return value[0:length]
