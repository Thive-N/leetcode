from collections import deque
from typing import List


class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        l = r = k
        result = minimum = nums[k]
        ln = len(nums)
        while l > 0 or r < ln-1:
            l1 = nums[l-1] if l > 0 else 0
            r1 = nums[r+1] if r < ln-1 else 0
            if l1 > r1:
                l -= 1
                minimum = min(minimum, l1)
            else:
                r += 1
                minimum = min(minimum, r1)

            result = max(result, (minimum*(r-l+1)))
        return result
