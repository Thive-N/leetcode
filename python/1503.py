from typing import List


class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        ml = 0 if len(left) == 0 else max(left)
        mr = n if len(right) == 0 else min(right)
        return max(ml, n - mr)
