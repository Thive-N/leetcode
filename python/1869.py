class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        max1 = 0
        max0 = 0
        c1 = 0
        c0 = 0

        for c in s:
            if c == '0':
                c1 = 0
                c0 += 1
                max0 = max(max0, c0)
                continue
            c0 = 0
            c1 += 1
            max1 = max(max1, c1)

        return max1 > max0

