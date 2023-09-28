class Solution(object):
    def plusOne(self, digits):
        digits = [str(x) for x in digits]
        digits = ''.join(digits)
        digits = int(digits)
        digits += 1
        digits = str(digits)
        digits = [int(x) for x in digits]
        return digits
