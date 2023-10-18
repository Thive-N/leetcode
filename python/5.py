class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s
        e = ""
        for si in range(len(s)):
            for ei in range(si, len(s)+1)[::-1]:
                slc = s[si:ei]
                if slc == slc[::-1]:
                    if len(e) < len(slc):
                        e = slc
                        break
        return e
