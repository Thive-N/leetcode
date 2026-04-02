class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = []
        for i,x in enumerate(nums):
            for ii,y in enumerate(nums):
                if x+y == target and i != ii:
                    ans = [i,ii]

        return ans