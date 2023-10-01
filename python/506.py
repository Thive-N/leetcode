from typing import List


class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        sort = sorted(score)[::-1]
        mapping = {}
        rmap = {}
        for i in range(len(sort)):
            mapping[sort[i]] = str(i+1)
            rmap[i+1] = sort[i]

        mapping[rmap[1]] = "Gold Medal"
        if 2 in rmap:
            mapping[rmap[2]] = "Silver Medal"
        if 3 in rmap:
            mapping[rmap[3]] = "Bronze Medal"

        end = []
        for x in score:
            end.append(mapping[x])

        return end


s = Solution()
print(s.findRelativeRanks([15, 654, 32, 653]))
