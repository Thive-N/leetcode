from typing import List


class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        r = [0, 0]
        index = 0
        while n:
            if n % 2 == 1:
                r[index % 2] += 1
            index += 1
            n = n >> 1
        return r
