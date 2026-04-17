mapping = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}


class Solution:
    def romanToInt(self, s: str) -> int:
        current = 0
        previous = 10000000000000000000000
        for x in s:            
            if mapping[x] > previous:
                current += mapping[x] - 2*previous
            else:
                current += mapping[x]
            previous = mapping[x]

        return current


s = Solution()
print(s.romanToInt("LVIII"))