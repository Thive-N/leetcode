class Solution:
    def fib(self, n: int) -> int:
        e = [0,1]
        list(map(lambda i: e.append(e[i-1] + e[i-2]), range(2, n+1)))
        return e[n]
