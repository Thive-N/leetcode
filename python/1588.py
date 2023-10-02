from typing import List


class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        n = len(arr)
        total = 0
        for i in range(1, n + 1):
            for j in range(n + 1 - i):
                temp = arr[j:j + i]
                if len(temp) % 2 == 1:
                    total += sum(temp)
        return total
