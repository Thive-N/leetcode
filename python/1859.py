class Solution:
    def sortSentence(self, s: str) -> str:
        words = s.split(" ")
        mapping = {}
        for x in words:
            pos = int(x[-1])
            word = x[:-1]
            mapping[pos] = word

        end = []

        for x in range(len(words)):
            end.append(mapping[x+1])

        return " ".join(end)
