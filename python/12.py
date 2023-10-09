class Solution:
    def intToRoman(self, num: int) -> str:
        thing = ""
        mapping = {
            1: "I",
            4: "IV",
            5: "V",
            9: "IX",
            10: "X",
            40: "XL",
            50: "L",
            90: "XC",
            100: "C",
            400: "CD",
            500: "D",
            900: "CM",
            1000: "M",
        }

        while num:
            for key in list(mapping.keys())[::-1]:
                if key <= num:
                    thing += mapping[key]
                    num -= key
                    break
        return thing


s = Solution()
print(s.intToRoman(1994))
