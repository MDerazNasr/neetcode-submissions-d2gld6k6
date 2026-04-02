class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        10,1,5,6,7,1]
        l    r
        '''
        l, r = 0,1
        maxProfit = 0

        while r < len(prices):
            if prices[r] > prices[l]:
                profit = prices[r] - prices[l]
                maxProfit = max(maxProfit, profit)
                r += 1
            else:
                l += 1
                r = l + 1
        return maxProfit

