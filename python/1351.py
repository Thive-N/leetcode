from typing import List


class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        return sum([x < 0 for y in grid for x in y])
