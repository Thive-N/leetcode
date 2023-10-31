from typing import List


class Solution:
    def closetTarget(self, words: List[str], target: str, startIndex: int) -> int:
        n = len(words)
        for i in range(n):
            if words[(startIndex + i + n) % n] == target:
                return i
            if words[(startIndex - i + n) % n] == target:
                return i
        return -1
