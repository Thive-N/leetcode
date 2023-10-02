from typing import List


class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        if len(arr) == 2:
            return True

        arr = sorted(arr)
        diff = arr[0] - arr[1]
        prev = arr[0]

        for x in arr[1:]:
            if prev-x != diff:
                return False
            prev = x
        return True
