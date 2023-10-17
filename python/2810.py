class Solution:
    def finalString(self, s: str) -> str:
        e = ""
        for x in s:
            if x == "i":
                e = e[::-1]
                continue
            e += x
        return e
