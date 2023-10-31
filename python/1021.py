class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        ans = []
        i = 0

        for c in s:
            if c == '(':
                i += 1
                if i > 1:
                    ans.append(c)
            else:
                i -= 1
                if i > 0:
                    ans.append(c)

        return ''.join(ans)
