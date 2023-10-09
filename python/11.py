from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        if not height:
            return 0
        m = 0

        l = 0
        r = len(height)-1

        while True:
            hl = height[l]
            hr = height[r]

            if l == r:
                break

            m = max(m, abs(l-r) * min(hl, hr))

            if hl < hr:
                l += 1
            elif hr < hl:
                r -= 1
            else:
                if height[l+1] > height[r-1]:
                    l += 1
                else:
                    r -= 1

            if m == 0:
                continue

            if abs(l-r) / m > max(height):
                return
        return m


s = Solution()
s.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7])
