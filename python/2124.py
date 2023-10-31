class Solution:
    def checkString(self, s: str) -> bool:
        return sorted(list(s)) == list(s)
