from typing import *


class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        s = set()
        for x in arr:
            if x * 2 in s or x / 2 in s:
                return True
            s.add(x)
        return False
