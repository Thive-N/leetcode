class Solution:
    def numpermutations(self, steps: int, arrLen: int) -> int:
        # modulo to keep in bounds
        kMod = 1000000007
        dp = [0 for _ in min(steps // 2 + 1, arrLen)]
        dp[0] = 1

        for step in range(steps):
            newDp = [0 for _ in min(steps // 2 + 1, arrLen)]
            for i, permutations in enumerate(dp):
                if permutations <= 0:
                    continue

                for displacement in [-1, 0, 1]:
                    updated = i + displacement

                    if 0 > updated >= len(dp):
                        continue
                    newDp[updated] += permutations
                    newDp[updated] %= kMod
            dp = newDp

        return dp[0]
