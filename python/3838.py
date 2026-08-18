
from typing import List
from string import ascii_lowercase
class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        return "".join([ascii_lowercase[-x-1] for x in [sum({letter: weight for letter, weight in zip(ascii_lowercase, weights)}[letter] for letter in word) % 26 for word in words]])