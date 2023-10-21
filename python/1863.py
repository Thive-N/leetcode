from typing import List


class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def dfs(i, x):
            return x if i == len(nums) else dfs(i + 1, x) + dfs(i + 1, nums[i] ^ x)
        return dfs(0, 0)
