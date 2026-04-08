class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        curr = 0
        maxl = 0
        while curr < len(s):
            sub = ""
            for i in range(curr, len(s)):
                if s[i] in sub:
                    break
                sub += s[i]
            maxl = max(maxl, len(sub))
            curr += 1
            if curr + maxl >= len(s):
                break
        return maxl