class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        stack = []
        for x in s:
           if x.isalpha():
               stack.append(x)

        s = list(s)
        for i,x in enumerate(s):
            if x.isalpha():
                s[i] = stack.pop(-1)

        return "".join(s)

