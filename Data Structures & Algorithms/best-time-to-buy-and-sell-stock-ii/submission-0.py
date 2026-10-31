class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        total_profit = 0
        profit=0

        for i in range(1, len(prices)):
            if prices[i]>prices[i-1]:
                profit = prices[i]-prices[i-1]
            total_profit+= profit
            profit=0
        return total_profit
