class Solution(object):
    def sortArrayByParity(self, nums):
        left = []
        right = []

        for num in nums:
            if num % 2 == 0:
                left.append(num)
            else:
                right.append(num)

        return left + right
