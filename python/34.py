from bisect import bisect_left, bisect_right
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        try:
            l = nums.index(target)
        except ValueError:
            return -1, -1

        r = len(nums) - nums[::-1].index(target) - 1
        # l = bisect_left(nums, target)
        # if l == len(nums) or nums[l] != target:
        #     return -1, -1
        # r = bisect_right(nums, target) - 1
        return l, r
