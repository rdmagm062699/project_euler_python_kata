
class IrrationalDecimalFraction:
    def __init__(self, length):
        digits = '0123456789'

        if length < 10:
            self.value = digits[1:length + 1]
        else:
            tempValue = '123456789'
            nextStart = 1
            while len(tempValue) < length:
                nextChunk = ''.join([str(nextStart) + digit for digit in digits])
                tempValue += nextChunk
                nextStart += 1

            self.value = tempValue[0:length]
