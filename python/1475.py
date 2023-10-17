class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        arr = []
        for x in range(len(prices)):
            y = 0
            for x2 in range(x+1,len(prices)):
                if prices[x2] <= prices[x]:
                    y = prices[x2]
                    break
            arr.append(prices[x] - y)
        return arr
