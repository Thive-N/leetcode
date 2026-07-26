from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if not triangle:
            return 0

        for i in range(len(triangle) - 1, 0, -1):
            for j in range(len(triangle[i]) - 1):
                triangle[i - 1][j] += min(triangle[i][j], triangle[i][j + 1])

        return triangle[0][0]
