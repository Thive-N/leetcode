class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        res = []
        for xx in range(len(words)):
            if x in words[xx]:
                res.append(xx)

        return res