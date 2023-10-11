class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        return sum([1 if x in jewels else 0 for x in stones])
