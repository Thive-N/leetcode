from typing import *


class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        delta = [0 for _ in range(len(s) + 1)]

        for start, end, direction in shifts:
            d = 1
            if direction == 0:
                d = -1

            delta[start] += d
            delta[end] -= d

        for i in range(1, len(delta)):
            delta[i] += delta[i - 1]

        a = ord('a')
        applied = []
        for i in range(len(s)):
            x = (ord(s[i]) - a + delta[i] + 26)
            x = a + x % 26
            applied.append(a+x)

        return "".join(map(chr, applied))


if __name__ == '__main__':
    s = Solution()
    print(s.shiftingLetters("abc", [[0, 1, 1], [1, 2, 2]]))
