class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        c = 0
        while n > 0:
            print(n)
            c += n % 2
            n = n >> 1
        return c == 1


s = Solution()
print(s.isPowerOfTwo(-16))
