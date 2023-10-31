from typing import List


class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        return [int(x) for y in nums for x in str(y)]
