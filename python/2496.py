from typing import List


class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        m = 0
        for x in strs:
            if x.isnumeric():
                m = max(m, int(x))
            else:
                m = max(m, len(x))
        return m
