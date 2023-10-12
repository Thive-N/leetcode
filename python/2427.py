import math


class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        return sum(a % x == 0 and b % x == 0 for x in range(1, math.gcd(a, b) + 1))
