class Solution:
    def maxScore(self, s: str) -> int:
        m = 0
        for i in range(1, len(s)):
            score = s[:i].count('0') + s[i:].count('1')
            m = max(m, score)
        return m
