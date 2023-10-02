from typing import List


class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        m = max(nums)
        return sum(range(m, m+k))
