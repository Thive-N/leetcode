from typing import List


class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        return len(set(map(lambda word: "".join([[".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."][ord(letter)-97] for letter in word]), words)))
