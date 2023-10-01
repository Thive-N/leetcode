from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        s = 0
        h = -999

        for price in prices:
            s = max(s, h + price)
            h = max(h, -price)
        return s


s = Solution()
print(s.maxProfit([7, 1, 5, 3, 6, 4]))
