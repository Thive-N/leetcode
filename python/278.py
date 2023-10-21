def isBadVersion(): pass


class Solution:
    def firstBadVersion(self, n: int) -> int:
        l = 1
        r = n

        while l < r:
            mid = (l + r)//2
            if isBadVersion(mid):
                r = mid
                continue
            l = mid + 1
        return l
