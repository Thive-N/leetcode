from typing import List
from collections import Counter


class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        count = Counter()
        for n in nums:
            for x in n:
                count[x] += 1

        return sorted([i for i, c in count.items()
                       if c == len(nums)])
