class Solution:
    def smallestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s

        # odd length
        if len(s) % 2 == 1:
            mid = len(s) // 2
            left = s[:mid]
            return "".join(sorted(left)) + s[mid] + "".join(sorted(left)[::-1])

        # even length
        mid = len(s) // 2
        left = s[:mid]
        return "".join(sorted(left)) + "".join(sorted(left)[::-1])