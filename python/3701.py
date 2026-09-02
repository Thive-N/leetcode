class Solution:
    def alternatingSum(self, nums: List[int]) -> int:
        ol = [0-x for x in nums[1::2]]
        el = nums[0::2]

        o = sum(ol)
        e = sum(el)
        return o+e