class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        e = 0
        while start > 0 or goal > 0:
            if start % 2 != goal % 2:
                e += 1
            start = start >> 1
            goal = goal >> 1
            
        return e

