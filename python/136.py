from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        for i in nums[1:]:
            nums[0] ^= i
        return nums[0]
