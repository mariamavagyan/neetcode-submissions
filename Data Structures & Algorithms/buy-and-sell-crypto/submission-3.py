class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        profit = n * [0]
        print('profit = ', profit)

        # for i in range(1, n):
        #     for j in range(i):
        #         # profit = current sell price - buy price
        #         cur_profit = prices[i] - prices[j]
        #         if cur_profit >= profit[i]:
        #             profit[i] = cur_profit
        # return max(profit)

        min_price = float('inf')
        max_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price
            else:
                cur_profit = price - min_price
                max_profit = max(max_profit, cur_profit)
        return max_profit


        