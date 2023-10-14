from typing import List


class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        sdn = []
        for i in range(left, right+1):
            if '0' in str(i):
                continue
            if sum([i % int(s) for s in str(i)]) == 0:
                sdn.append(i)

        return sdn
