class Solution:
    def minElement(self, nums: List[int]) -> int:
        if not nums:
            return -1  # Return -1 for empty list

        return min(sum(int(digit) for digit in str(x)) for x in nums)