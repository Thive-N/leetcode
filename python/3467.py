class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        return sorted([1 if x%2 != 0 else 0 for x in nums])