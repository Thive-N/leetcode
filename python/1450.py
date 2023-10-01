from typing import List


class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        return sum([1 if x <= queryTime and queryTime <= y else 0 for x, y in zip(startTime, endTime)])
