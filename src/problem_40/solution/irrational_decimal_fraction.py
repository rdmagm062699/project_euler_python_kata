
class IrrationalDecimalFraction:
    def __init__(self, length):
        digits = '0123456789'

        if length < 10:
            self.value = digits[1:length + 1]
        else:
            tempValue = '123456789'
            nextChunk = ''.join(['1' + digit for digit in digits])
            self.value = tempValue + nextChunk
