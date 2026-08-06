
from typing import List
from string import ascii_lowercase
class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        word_weight_map = {letter: weight for letter, weight in zip(ascii_lowercase, weights)}
        return "".join([ascii_lowercase[-x-1] for x in [sum(word_weight_map[letter] for letter in word) % 26 for word in words]])