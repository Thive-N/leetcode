from typing import List
from collections import Counter


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        c = Counter(nums)
        for i in range(1, 101):
            c[i] += c[i - 1]
        return [0 if num == 0 else c[num - 1] for num in nums]
