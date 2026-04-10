class Solution:
    def reverse(self, x: int) -> int:
        b = int(str(abs(x))[::-1])
        x = b if x >= 0 else -b
        return x if abs(x) <= 2147483647 else 0