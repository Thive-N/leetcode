from typing import List
import collections


class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        dp = [0 for _ in range(len(nums))]
        ans = -999999999999999
        queue = collections.deque()

        for i, x in enumerate(nums):
            if queue and (i - queue[0]) > k:
                queue.popleft()
            dp[i] = max(0, 0 if not queue else dp[queue[0]]) + x
            while queue and dp[queue[-1]] <= dp[i]:
                queue.pop()
            queue.append(i)
            ans = max(ans, dp[i])

        return ans
