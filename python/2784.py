from typing import List
from collections import *


class Solution:
    def isGood(self, nums: List[int]) -> bool:
        count = Counter(nums)
        return all(count[i] == 1 for i in range(1, len(nums) - 1)) and count[len(nums) - 1] == 2
