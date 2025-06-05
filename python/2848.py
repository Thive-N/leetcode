from typing import List


class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        m1 = [0] * 100
        for s, e in nums:
            for x in range(s-1, e):
                m1[x] = 1

        return sum(m1)
