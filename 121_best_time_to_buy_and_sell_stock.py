# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

class Solution():
    def maxProfit(self, prices):
        buy = prices[0]
        profit = 0

        for i in range(1, len(prices)):
            print(i , prices[i], buy)
            if prices[i] < buy:
                buy = prices[i]
            elif prices[i] - buy > profit:
                profit = prices[i] - buy

        print(profit)
        return profit
sols = Solution()
sols.maxProfit([7,1,5,3,6,4])
