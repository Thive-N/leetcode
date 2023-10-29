class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        pow = int(minutesToTest / minutesToDie + 1)
        ans = 0
        while pow ** ans < buckets:
            ans += 1
        return ans
