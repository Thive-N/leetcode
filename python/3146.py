class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        index_map = {char: i for i, char in enumerate(s)}
        difference = 0

        for i, char in enumerate(t):
            difference += abs(i - index_map[char])

        return difference
