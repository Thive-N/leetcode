class Solution:
    def toHex(self, num: int) -> str:
        mapping = ['0', '1', '2', '3', '4', '5', '6',
                   '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
        ans = ""

        if num == 0:
            return '0'

        if num > 0:
            while num:
                ans += mapping[num % 16]
                num >>= 4
        else:
            for _ in range(8):
                ans += mapping[num & 15]
                num >>= 4

        return ans[::-1]


s = Solution()
print(s.toHex(26))
