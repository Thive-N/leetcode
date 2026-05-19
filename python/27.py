class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        new = list(filter((val).__ne__, nums))
        for i,x in enumerate(new):
            nums[i] = x
        return len(new)