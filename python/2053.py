from typing import List


class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        count = {x: arr.count(x) for x in arr}

        for a in arr:
            if count[a] == 1:
                k -= 1
                if k == 0:
                    return a

        return ''
