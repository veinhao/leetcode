class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        # max = 0
        # for i in range(len(prices) - 1):
        #     for j in range(i + 1, len(prices)):
        #         if prices[i] >= prices[j]:
        #             continue
        #         if prices[i] < prices[j] and prices[j] - prices[i] > max:
        #             max = prices[j] - prices[i]
        #
        # return max
        min_ = prices[0]
        max_price = 0
        for i in range(1, len(prices)):
            if min_ > prices[i]:
                min_ = prices[i]

            if prices[i] - min_ > max_price:
                max_price = prices[i] - min_

        return max_price


