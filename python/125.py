class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = [x for x in s.lower() if x.isalnum()]
        print(n)
        return n == n[::-1]


s = Solution()
print(s.isPalindrome("0P"))
