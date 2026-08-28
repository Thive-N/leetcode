class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        odd_sum = sum(i for i in range(1, n + 1) if i % 2 != 0)
        even_sum = sum(i for i in range(1, n + 1) if i % 2 == 0)
        
        def gcd(a: int, b: int) -> int:
            while b:
                a, b = b, a % b
            return a
        
        return gcd(odd_sum, even_sum)