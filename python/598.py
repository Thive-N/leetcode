from typing import List


class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        Y = m
        X = n

        for y, x in ops:
            Y = min(Y, y)
            X = min(X, x)

        return X * Y
