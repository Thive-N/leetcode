from typing import List


class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        left = [sum(nums[:i]) for i in range(len(nums))]
        right = [sum(nums[i+1:]) for i in range(len(nums))]
        return [abs(x-y) for x, y in zip(left, right)]
