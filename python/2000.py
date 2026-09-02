class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if ch not in word:
            return word
        r,x = word.split(ch,1)
        return "".join([ch,r[::-1],x])