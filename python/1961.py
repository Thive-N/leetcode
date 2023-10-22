from typing import List


class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        i = 0
        for c, word in enumerate(words):
            i += len(word)
            if len(s) == i:
                return ''.join(words[:c+1]) == s
        return False
