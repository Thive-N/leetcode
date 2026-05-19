
class Solution:
    def divide(self, x: int, y: int) -> int:
        return min(max(-2147483648, int(x/y)), 2147483647)