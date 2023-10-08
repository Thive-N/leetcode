from typing import List


class Solution:
    def maxDotProduct(self, A: List[int], B: List[int]) -> int:
        m = len(A)
        n = len(B)

        neginf = -(10**60)
        # initialise an empty matrix with 1 extra index to store -inf
        # so that negative numbers can be multiplied and found without it affecting it like 0 would
        dp = [[neginf] * (n + 1) for _ in range(m + 1)]

        # for every index in A
        for i in range(m):
            # for every index in B
            for j in range(n):
                # take the max between zero and dp[i][j] this will be zero on the first iteration
                # set temp as the product between a[i] and b[j]
                temp = max(0, dp[i][j]) + A[i] * B[j]

                # set the next i and j index to be the max of the value above the value to the left or temp calculated above
                # dp[i + 1][j + 1] works as we initialised this array with an extra index
                dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j], temp)

        # solution will cascade into having the biggest number at dp[m][n]
        return dp[m][n]


s = Solution()
ans = s.maxDotProduct([2, 1, -2, 5], [3, 0, -6])
print(ans)
