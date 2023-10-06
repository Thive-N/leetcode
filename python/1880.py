class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        def cnv(x): return int("".join([str(ord(i) - ord('a')) for i in x]))
        return cnv(firstWord) + cnv(secondWord) == cnv(targetWord)
