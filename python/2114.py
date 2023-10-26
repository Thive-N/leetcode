from typing import List


class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        return max(len(s.split(" ")) for s in sentences)
