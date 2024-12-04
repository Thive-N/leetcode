from typing import *


class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        for i, x in enumerate(sentence.split(" ")):
            if x.startswith(searchWord):
                return i + 1
        return -1


if __name__ == "__main__":
    sentence = "i love eating burger"
    searchWord = "burg"
    s = Solution()
    print(s.isPrefixOfWord(sentence, searchWord))
