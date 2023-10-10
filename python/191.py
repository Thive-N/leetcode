class Solution:
    def hammingWeight(self, n: int) -> int:
        return len(list(filter(lambda x: x == "1", str(bin(n)[2:]))))
