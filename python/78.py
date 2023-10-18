from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def dfs(curr=[], depth=0):
            ans.append(curr)

            for i in range(depth, len(nums)):
                dfs(curr+[nums[i]], i+1)

        dfs()
        return ans
