from typing import List


class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        return [x for word in words for x in word.split(separator) if x != ""]
