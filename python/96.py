class Solution:
    def numTrees(self, n: int) -> int:
        dp = [1] * (n + 1)
        for nodes in range(2, n+1):

            total = 0
            # for every permutation of node
            for node in range(1,nodes+1):
                L = node - 1
                R = nodes - node
                total += dp[L] * dp[R]
            dp[nodes] = total
        return dp[n]

if __name__ == "__main__":
    s = Solution()
    print(s.numTrees(20))