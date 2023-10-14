from typing import List


class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        c = {}

        def re(i, r):
            if r <= 0:
                return 0
            if i == len(cost):
                return float("inf")
            if (i, r) in c:
                return c[(i, r)]
            paint = cost[i] + re(i+1, r-1-time[i])
            skip = re(i+1, r)
            c[(i, r)] = min(paint, skip)
            return c[(i, r)]

        return re(0, len(cost))
