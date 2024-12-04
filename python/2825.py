from typing import *
from collections import *


class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        q = deque(str2)
        for x in str1:
            new = chr(((ord(x) - 96) % 26) + 97)
            if len(q) > 0 and (q[0] in [x, new]):
                q.popleft()

        return len(q) == 0


if __name__ == "__main__":
    s = Solution()
    print(s.canMakeSubsequence("zc", "ad"))
