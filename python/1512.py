from typing import List


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = [0]*101
        ans = 0
        for x in nums:
            ans += count[x]
            count[x] += 1

        return ans
