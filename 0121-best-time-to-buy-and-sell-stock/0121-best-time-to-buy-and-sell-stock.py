class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # n = len(prices) 
        # profit_temp = 0
        # for i in range(n):
        #     for j in range(i + 1, n):
        #         if prices[j] > prices[i]:
        #             temp = prices[j] - prices[i]
        #             profit_temp = max(profit_temp,temp)

        # return profit_temp
        
        min_price = float('inf')
        max_profit = 0
        for price in prices:
            if price < min_price:
                min_price = price

            elif price - min_price > max_profit:
                max_profit = price - min_price

        return max_profit
