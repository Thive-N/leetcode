class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        # combine even and odd index arrays
        freq = [0] * 52

        for i, (a, b) in enumerate(zip(s1, s2)):
            # offset for even or odd array
            array = (i & 1) * 26
            freq[ord(a) - 97 + array] += 1
            freq[ord(b) - 97 + array] -= 1

        return all(c == 0 for c in freq)