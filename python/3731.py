class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        nums.sort()
        starting = nums[0]
        ending = nums[-1]

        arr = set(nums)
        arr1 = []

        for i in range(starting, ending + 1):
            if i not in arr:
                arr1.append(i)

        return arr1