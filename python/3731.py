class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(n):
            index = abs(nums[i]) - 1
            if nums[index] > 0:
                nums[index] = -nums[index]
        return [i + 1 for i in range(n) if nums[i] > 0]