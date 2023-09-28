class Solution(object):
    def climbStairs(self, n):
        if n == 1:
            return 1
        else:
            a = 1
            b = 2
            for i in range(n - 2):
                a, b = b, a + b
            return b
