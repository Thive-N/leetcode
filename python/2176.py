from typing import List


class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        c = 0
        for x in range(len(nums)):
            for y in range(x+1, len(nums)):
                if nums[x] != nums[y]:
                    continue
                if (x*y) % k == 0:
                    c += 1
        return c
