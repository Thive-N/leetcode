from typing import List


class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        ans = [pref[0]] + [0] * (len(pref) - 1)
        for i in range(1, len(ans)):
            ans[i] = pref[i] ^ pref[i - 1]

        return ans
