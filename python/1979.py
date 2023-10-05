from typing import List


class Solution:
    def findGCD(self, nums: List[int]) -> int:
        m1 = min(nums)
        m2 = max(nums)
        for x in range(1001, 1, -1):
            if m1 % x or m2 % x:
                continue
            return x
        return 1
