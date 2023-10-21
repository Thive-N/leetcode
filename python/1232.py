from typing import List


class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        dx = (coordinates[1][0] - coordinates[0][0])
        dy = (coordinates[1][1] - coordinates[0][1])

        return all((x - coordinates[0][0]) * dy == (y - coordinates[0][1]) * dx for x, y in coordinates)
