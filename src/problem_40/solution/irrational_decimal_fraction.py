
class IrrationalDecimalFraction:
    def __init__(self, length):
        self.value = ''

        integers = '123456789'

        if length > 0:
            self.value = integers[0:length]
