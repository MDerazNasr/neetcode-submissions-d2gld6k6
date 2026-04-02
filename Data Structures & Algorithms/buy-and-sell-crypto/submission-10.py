class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        maxProfit = 0

        for r in range(len(prices)):
            profit = prices[r] - prices[l]
            if prices[l] > prices[r]:
                l = r
            maxProfit = max(maxProfit, profit)
            r += 1
        return maxProfit
        