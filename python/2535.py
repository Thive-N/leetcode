from typing import List


class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        return abs(sum([item for sublist in [[int(d) for d in str(n)] for n in nums] for item in sublist]) - sum(nums))
