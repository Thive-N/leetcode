
# nCr = n!/((n-r)!*r!)
from typing import List
from math import factorial


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ret = []
        for n in range(numRows):
            sublist = []
            for m in range(n+1):
                sublist.append(
                    int(factorial(n)/((factorial(n-m))*factorial(m))))
            ret.append(sublist)
        return ret
