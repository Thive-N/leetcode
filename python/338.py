from typing import List


class Solution:
    def countBits(self, b: int) -> List[int]:
        l = []
        for n in range(b+1):
            c = 0
            while n != 0:
                c += n % 2
                n = n >> 1
            l.append(c)
        return c
