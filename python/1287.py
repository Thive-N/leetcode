from typing import List
from collections import Counter


class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        return Counter(arr).most_common(1)[0][0]
