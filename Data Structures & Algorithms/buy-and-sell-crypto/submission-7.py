class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        maxProfit = 0

        for r in range(len(prices)):
            if r == 0:
                continue
            
            profit = prices[r] - prices[l]
            if prices[l] > prices[r]:
                l = r
            maxProfit = max(maxProfit, profit)

        return maxProfit