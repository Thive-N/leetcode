class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        m = {' ': ' '}
        count = 97
        for c in key:
            if c in m:
                continue
            m[c] = chr(count)
            count += 1
        return ''.join([m[c] for c in message])
