from typing import List


class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        return [a for freq, val in [nums[i:i + 2] for i in range(0, len(nums), 2)] for a in [val]*freq]
