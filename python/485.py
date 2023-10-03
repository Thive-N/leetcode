from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        return max([sum([int(y) for y in x]) for x in ("".join(str(x) for x in nums)).split("0")])
