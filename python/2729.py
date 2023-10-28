class Solution:
    def isFascinating(self, n):
        return ''.join(sorted(str(n) + str(2 * n) + str(3 * n))) == '123456789'
