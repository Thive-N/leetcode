from typing import List
from collections import Counter, defaultdict
from string import ascii_letters


class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        def isMatch(word):
            wordCount = Counter(word)
            return False if any(wordCount[i] < count[i] for i in ascii_letters) else True

        ans = ' ' * 15
        count = defaultdict(int)

        for c in licensePlate:
            if c.isalpha():
                count[c.lower()] += 1

        for word in words:
            if len(word) < len(ans) and isMatch(word):
                ans = word

        return ans
