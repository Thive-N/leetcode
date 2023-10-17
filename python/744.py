from typing import List


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        for x in letters:
            if ord(target) < ord(x):
                return x

        return letters[0]
