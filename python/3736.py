class Solution:
    def minMoves(self, nums: List[int]) -> int:
        x = max(nums)
        sum = 0
        for i in range(len(nums)):
            xx = x - nums[i]
            sum += xx
        return sum