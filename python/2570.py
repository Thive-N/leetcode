from typing import List
from collections import defaultdict


class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        cnt = defaultdict(int)
        for i, v in nums1 + nums2:
            cnt[i] += v
        return [x[1] for x in sorted(cnt.items())]
