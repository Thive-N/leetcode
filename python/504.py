class Solution:
    def convertToBase7(self, num: int) -> str:
        if num < 0:
            return '-' + self.convertToBase7(-num)
        else:
            frac = num % 7
            rest = num // 7
            return self.convertToBase7(rest) + str(frac) if rest else str(frac)