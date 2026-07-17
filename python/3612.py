class Solution:
    def processStr(self, s: str) -> str:
        res = ""
        for c in s:
            if c.islower():
                res += c
            if c == '#':
                res = res + res
            if c == '%':
                res = res[::-1]
            if c == '*':
                res = res[:-1]
        return res