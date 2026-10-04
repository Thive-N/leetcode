class Solution:
    def checkValidString(self, s: str) -> bool:
        mn = 0
        mx = 0

        for c in reversed(s):
            mn += (c == ')') - (c == '(') - (c == '*')
            mx += (c == ')') - (c == '(') + (c == '*')

            if mx < 0:
                return False

            mn = max(mn, 0)

        return mn == 0