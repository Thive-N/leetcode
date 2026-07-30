class Solution:
    def minimumPushes(self, word: str) -> int:
        return ((len(word)//8)*((len(word)//8)+1)*4)+((len(word)%8)*((len(word)//8)+1))