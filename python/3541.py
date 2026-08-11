class Solution:
    def maxFreqSum(self, s: str) -> int:
        freq = {}
        for char in s:
            freq[char] = freq.get(char, 0) + 1


        maxvowelfreq = 0
        maxconsonantfreq = 0
        for char, count in freq.items():
            if char in 'aeiou':
                maxvowelfreq = max(maxvowelfreq, count)
            else:
                maxconsonantfreq = max(maxconsonantfreq, count)

        return maxvowelfreq + maxconsonantfreq