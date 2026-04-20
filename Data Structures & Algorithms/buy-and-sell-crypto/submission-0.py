class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxAns = 0
        minBuy = prices[0]
        maxSell = prices[0]
        for i in range(len(prices)):
            if prices[i] < minBuy:
                minBuy = prices[i]
                maxSell = prices[i]
            else:
                maxSell = max(maxSell, prices[i])
            maxAns = max(maxAns, maxSell - minBuy)
        return maxAns