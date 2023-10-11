from typing import List


class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        return sum([0 if list(sorted(x)) == x else 1 for x in list(map(list, zip(*strs)))])


s = Solution()
print(s.minDeletionSize(["a", "b"]))
