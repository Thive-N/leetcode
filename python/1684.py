from typing import List


class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        return sum(all(char in set(allowed) for char in word) for word in words)
