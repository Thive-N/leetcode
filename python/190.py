class Solution:
    def reverseBits(self, n):
        n = bin(n)[2:]
        n = n[::-1]
        n = n + '0' * (32 - len(n))
        return int(n, 2)
