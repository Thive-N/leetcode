class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        chunks = [s[x:x+k] for x in range(0, len(s), k)]
        for i in range(0, len(chunks), 2):
            chunks[i] = chunks[i][::-1]
        return ''.join(chunks)