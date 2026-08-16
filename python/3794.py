class Solution:
    def reversePrefix(self, s: str, k: int) -> str:
        prefix = s[:k]
        reversed_prefix = prefix[::-1]
        return reversed_prefix + s[k:]