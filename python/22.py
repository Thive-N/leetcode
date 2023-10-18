class Solution:
    def generateParenthesis(self, n):
        ans = []

        def dfs(l: int, r: int, s: str):
            # number of brackets acheived base case
            if l == 0 and r == 0:
                ans.append(s)
            # open a bracket to close new branch in tree
            if l > 0:
                dfs(l - 1, r, s + '(')
            # close a bracket
            if l < r:
                dfs(l, r - 1, s + ')')

        dfs(n, n, '')
        return ans
