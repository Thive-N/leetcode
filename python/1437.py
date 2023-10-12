from typing import List


class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        ls = 99999999999999
        for x in nums:
            if x == 1:
                if ls < k:
                    return False
                ls = 0
                continue
            else:
                ls += 1

        return True
