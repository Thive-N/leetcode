from typing import List


class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        ms = 0
        cm = 0

        for rectangle in rectangles:
            sw = min(rectangle)
            if sw > cm:
                cm = sw
                ms = 1

            elif sw == cm:
                ms += 1
        return ms
