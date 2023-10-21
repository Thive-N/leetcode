class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        c = numBottles
        while numBottles >= numExchange:
            c += numBottles//numExchange
            numBottles = numBottles // numExchange + numBottles % numExchange
        return c
