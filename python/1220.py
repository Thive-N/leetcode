class Solution:
    def countVowelPermutation(self, n: int) -> int:
        f = [1] * 5
        mod = 1000000007
        for _ in range(n - 1):
            temp = [0, 0, 0, 0, 0]
            temp[0] = (f[1] + f[2] + f[4]) % mod
            temp[1] = (f[0] + f[2]) % mod
            temp[2] = (f[1] + f[3]) % mod
            temp[3] = f[2]
            temp[4] = (f[2] + f[3]) % mod
            f = temp
        return sum(f) % mod
