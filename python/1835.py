from typing import List


class Solution:
    def getXORSum(self, arr1: List[int], arr2: List[int]) -> int:
        a1 = arr1[0]
        a2 = arr2[0]
        for x in arr1[1:]:
            a1 ^= x
        for x in arr2[1:]:
            a2 ^= x

        return a1 & a2
