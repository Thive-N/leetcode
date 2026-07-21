class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
      nums.sort()
      r = []
      for i in range(len(nums)-1):
        if nums[i] == nums[i+1]:
          r.append(nums[i])
      return r