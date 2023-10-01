from typing import List
from math import factorial


class Solution:
    def getRow(self, n: int) -> List[int]:
        sublist = []
        for m in range(n+1):
            sublist.append(
                int(factorial(n)/((factorial(n-m))*factorial(m))))

        return sublist
