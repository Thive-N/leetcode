class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        hd = 0
        while x or y:
            if x % 2 != y % 2:
                hd += 1
            x = x >> 1
            y = y >> 1
        return hd
