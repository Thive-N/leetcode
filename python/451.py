class Solution:
    def frequencySort(self, s: str) -> str:
        return "".join(sorted(s, key=lambda x: -s.count(x)))
