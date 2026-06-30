class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        freq = {'a': 0, 'b': 0, 'c': 0}
        left = 0
        ans = 0
        n = len(s)

        for right in range(n):
            freq[s[right]] += 1

            while freq['a'] and freq['b'] and freq['c']:
                ans += n - right
                freq[s[left]] -= 1
                left += 1

        return ans