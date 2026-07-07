class Solution:
    def sumAndMultiply(self, n: int) -> int:
        return int(''.join(i for i in str(n) if i != '0')) * sum(int(i) for i in str(n) if i != '0') if n != 0 else 0