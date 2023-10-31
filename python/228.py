from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ans = []

        i = 0
        while i < len(nums):
            # get range
            start = nums[i]
            while i < len(nums) - 1 and nums[i] == nums[i + 1] - 1:
                i += 1
            end = nums[i]

            if start == end:
                ans.append(str(start))
            else:
                ans.append(str(start) + "->" + str(end))

            i += 1

        return ans
