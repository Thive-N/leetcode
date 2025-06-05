from typing import *


class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        while len(nums) > 1:
            temp = []
            prev = nums[0]
            for x in nums[1:]:
                temp.append((prev+x) % 10)
                prev = x

            nums = temp

        return nums[0]
