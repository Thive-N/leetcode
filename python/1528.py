from typing import List


class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        n = [""] * len(s)
        for i in range(len(s)):
            n[indices[i]] = s[i]
        return "".join(n)
