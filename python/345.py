class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a','e','i','o','u']
        rev = []
        s = list(s)
        for x in s:
            if x.lower() in vowels:
                rev.append(x)
        rev = rev[::-1]
        for x in range(len(s)):
            if s[x].lower() in vowels:
                s[x] = rev[0]
                rev.pop(0)
        return "".join(s)
