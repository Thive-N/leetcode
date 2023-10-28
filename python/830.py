from typing import List


class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        n = len(s)
        ans = []
        x = y = 0

        while x < n:
            while y < n and s[y] == s[x]:
                y += 1
            if y - x > 4:
                ans.append([x, y - 1])
            x = y

        return ans
