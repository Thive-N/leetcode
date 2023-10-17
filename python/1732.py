from typing import List 


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        alt = 0
        ma = alt
        for x in gain:
            alt += x
            ma = max(ma,alt)
        return ma
