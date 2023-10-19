from typing import List
import collections


class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        count = collections.Counter()
        count.update(set(nums1))
        count.update(set(nums2))
        count.update(set(nums3))
        return [x for x, c in count.items() if c >= 2]
