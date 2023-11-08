from typing import List
from collections import Counter


class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        return [word for word, freq in Counter((A + ' ' + B).split()).items() if freq == 1]
